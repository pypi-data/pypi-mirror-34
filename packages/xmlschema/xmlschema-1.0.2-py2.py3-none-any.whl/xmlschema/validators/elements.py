# -*- coding: utf-8 -*-
#
# Copyright (c), 2016-2018, SISSA (International School for Advanced Studies).
# All rights reserved.
# This file is distributed under the terms of the MIT License.
# See the file 'LICENSE' in the root directory of the present
# distribution, or http://opensource.org/licenses/MIT.
#
# @author Davide Brunato <brunato@sissa.it>
#
"""
This module contains classes for XML Schema elements, complex types and model groups.
"""
from decimal import Decimal

from ..compat import unicode_type
from ..exceptions import XMLSchemaAttributeError
from ..etree import etree_element, is_etree_element
from ..converters import ElementData
from ..qnames import (
    XSD_GROUP_TAG, XSD_SEQUENCE_TAG, XSD_ALL_TAG, XSD_CHOICE_TAG, XSD_ATTRIBUTE_GROUP_TAG,
    XSD_COMPLEX_TYPE_TAG, XSD_SIMPLE_TYPE_TAG, XSD_ALTERNATIVE_TAG, XSD_ELEMENT_TAG, XSD_ANY_TYPE,
    XSD_UNIQUE_TAG, XSD_KEY_TAG, XSD_KEYREF_TAG, XSI_NIL, XSI_TYPE, reference_to_qname, get_qname
)
from ..xpath import ElementPathMixin
from .exceptions import (
    XMLSchemaValidationError, XMLSchemaParseError, XMLSchemaChildrenValidationError
)
from .parseutils import get_xsd_attribute, get_xsd_bool_attribute, get_xsd_derivation_attribute
from .xsdbase import XsdComponent, XsdDeclaration, XsdType, ParticleMixin, ValidatorMixin
from .constraints import XsdUnique, XsdKey, XsdKeyref
from .wildcards import XsdAnyElement


XSD_MODEL_GROUP_TAGS = {XSD_GROUP_TAG, XSD_SEQUENCE_TAG, XSD_ALL_TAG, XSD_CHOICE_TAG}
XSD_ATTRIBUTE_GROUP_ELEMENT = etree_element(XSD_ATTRIBUTE_GROUP_TAG)


class XsdElement(XsdDeclaration, ValidatorMixin, ParticleMixin, ElementPathMixin):
    """
    Class for XSD 1.0 'element' declarations.
    
    <element
      abstract = boolean : false
      block = (#all | List of (extension | restriction | substitution))
      default = string
      final = (#all | List of (extension | restriction))
      fixed = string
      form = (qualified | unqualified)
      id = ID
      maxOccurs = (nonNegativeInteger | unbounded)  : 1
      minOccurs = nonNegativeInteger : 1
      name = NCName
      nillable = boolean : false
      ref = QName
      substitutionGroup = QName
      type = QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, ((simpleType | complexType)?, (unique | key | keyref)*))
    </element>
    """
    def __init__(self, elem, schema, name=None, is_global=False):
        super(XsdElement, self).__init__(elem, schema, name, is_global)
        if not hasattr(self, 'type'):
            raise XMLSchemaAttributeError("undefined 'type' attribute for %r." % self)
        if not hasattr(self, 'qualified'):
            raise XMLSchemaAttributeError("undefined 'qualified' attribute for %r." % self)

    def __setattr__(self, name, value):
        if name == "type":
            assert value is None or isinstance(value, XsdType), "Wrong value %r for attribute 'type'." % value
            if hasattr(value, 'attributes'):
                self.attributes = value.attributes
            else:
                self.attributes = self.schema.BUILDERS.attribute_group_class(
                    elem=XSD_ATTRIBUTE_GROUP_ELEMENT, schema=self.schema
                )
        super(XsdElement, self).__setattr__(name, value)

    def _parse(self):
        XsdComponent._parse(self)
        self._parse_attributes()
        index = self._parse_type()
        if self.type is None:
            self.type = self.maps.lookup_type(XSD_ANY_TYPE)

        self._parse_constraints(index)
        self._parse_substitution_group()

    def _parse_attributes(self):
        self._parse_particle()
        self.name = None
        self._ref = None
        self.qualified = self.elem.get('form', self.schema.element_form_default) == 'qualified'

        if self.default is not None and self.fixed is not None:
            self._parse_error("'default' and 'fixed' attributes are mutually exclusive", self)
        self._parse_properties('abstract', 'block', 'final', 'form', 'nillable')

        # Parse element attributes
        try:
            element_name = reference_to_qname(self.elem.attrib['ref'], self.namespaces)
        except KeyError:
            # No 'ref' attribute ==> 'name' attribute required.
            try:
                if self.is_global or self.qualified:
                    self.name = get_qname(self.target_namespace, self.elem.attrib['name'])
                else:
                    self.name = self.elem.attrib['name']
            except KeyError:
                self._parse_error("missing both 'name' and 'ref' attributes.")

            if self.is_global:
                if 'minOccurs' in self.elem.attrib:
                    self._parse_error("attribute 'minOccurs' not allowed for a global element.")
                if 'maxOccurs' in self.elem.attrib:
                    self._parse_error("attribute 'maxOccurs' not allowed for a global element.")
        else:
            # Reference to a global element
            if self.is_global:
                self._parse_error("an element reference can't be global.")
            for attribute in ('name', 'type', 'nillable', 'default', 'fixed', 'form', 'block'):
                if attribute in self.elem.attrib:
                    self._parse_error("attribute %r is not allowed when element reference is used." % attribute)
            xsd_element = self.maps.lookup_element(element_name)
            self._ref = xsd_element
            self.name = xsd_element.name
            self.type = xsd_element.type
            self.qualified = xsd_element.qualified

    def _parse_type(self):
        if self.ref:
            if self._parse_component(self.elem, required=False, strict=False) is not None:
                self._parse_error("element reference declaration can't has children.")
        elif 'type' in self.elem.attrib:
            type_qname = reference_to_qname(self.elem.attrib['type'], self.namespaces)
            try:
                self.type = self.maps.lookup_type(type_qname)
            except KeyError:
                self._parse_error('unknown type %r' % self.elem.attrib['type'])
                self.type = self.maps.lookup_type(XSD_ANY_TYPE)
        else:
            child = self._parse_component(self.elem, required=False, strict=False)
            if child is not None:
                if child.tag == XSD_COMPLEX_TYPE_TAG:
                    self.type = self.schema.BUILDERS.complex_type_class(child, self.schema)
                elif child.tag == XSD_SIMPLE_TYPE_TAG:
                    self.type = self.schema.BUILDERS.simple_type_factory(child, self.schema)
                return 1
            else:
                self.type = None
        return 0

    def _parse_constraints(self, index=0):
        self.constraints = {}
        for child in self._iterparse_components(self.elem, start=index):
            if child.tag == XSD_UNIQUE_TAG:
                constraint = XsdUnique(child, self.schema, parent=self)
            elif child.tag == XSD_KEY_TAG:
                constraint = XsdKey(child, self.schema, parent=self)
            elif child.tag == XSD_KEYREF_TAG:
                constraint = XsdKeyref(child, self.schema, parent=self)
            else:
                raise XMLSchemaParseError("unexpected child element %r:" % child, self)

            try:
                if child != self.maps.constraints[constraint.name]:
                    self._parse_error("duplicated identity constraint %r:" % constraint.name, child)
            except KeyError:
                self.maps.constraints[constraint.name] = child
            finally:
                self.constraints[constraint.name] = constraint

    def _parse_substitution_group(self):
        substitution_group = self.substitution_group
        if substitution_group is None:
            return

        if not self.is_global:
            self._parse_error("'substitutionGroup' attribute in a local element declaration")

        qname = reference_to_qname(substitution_group, self.namespaces)
        if qname[0] != '{':
            qname = get_qname(self.target_namespace, qname)
        try:
            head_element = self.maps.lookup_element(qname)
        except KeyError:
            self._parse_error("unknown substitutionGroup %r" % substitution_group)
        else:
            final = head_element.final
            if final is None:
                final = self.schema.final_default

            if final == '#all' or 'extension' in final and 'restriction' in final:
                self._parse_error("head element %r cannot be substituted." % head_element)
            elif self.type == head_element.type or self.type.name == XSD_ANY_TYPE:
                pass
            elif 'extension' in final and not self.type.is_derived(head_element.type, 'extension'):
                self._parse_error(
                    "%r type is not of the same or an extension of the head element %r type."
                    % (self, head_element)
                )
            elif 'restriction' in final and not self.type.is_derived(head_element.type, 'restriction'):
                self._parse_error(
                    "%r type is not of the same or a restriction of the head element %r type."
                    % (self, head_element)
                )
            elif not self.type.is_derived(head_element.type):
                self._parse_error(
                    "%r type is not of the same or a derivation of the head element %r type."
                    % (self, head_element)
                )

    def _validation_error(self, error, validation, obj=None):
        if not isinstance(error, XMLSchemaValidationError):
            error = XMLSchemaValidationError(self, obj, reason=unicode_type(error))

        if error.schema_elem is None:
            if self.type.name is not None and self.target_namespace == self.type.target_namespace:
                error.schema_elem = self.type.elem
            else:
                error.schema_elem = self.elem
        if error.elem is None and is_etree_element(obj):
            error.elem = obj
        return super(XsdElement, self)._validation_error(error, validation)

    @property
    def built(self):
        return self.type.is_global or self.type.built

    @property
    def validation_attempted(self):
        if self.built:
            return 'full'
        else:
            return self.type.validation_attempted

    @property
    def admitted_tags(self):
        return {XSD_ELEMENT_TAG}

    # Properties inherited by references
    @property
    def abstract(self):
        if self._ref is not None:
            return self._ref.abstract
        return get_xsd_bool_attribute(self.elem, 'abstract', default=False)

    @property
    def default(self):
        return self.elem.get('default') if self._ref is None else self._ref.default

    @property
    def fixed(self):
        return self.elem.get('fixed') if self._ref is None else self._ref.fixed

    @property
    def form(self):
        if self._ref is not None:
            return self._ref.form
        return get_xsd_attribute(self.elem, 'form', ('qualified', 'unqualified'), default=None)

    @property
    def nillable(self):
        if self._ref is not None:
            return self._ref.nillable
        return get_xsd_bool_attribute(self.elem, 'nillable', default=False)

    # Global element's exclusive properties
    @property
    def final(self):
        return get_xsd_derivation_attribute(self.elem, 'final', ('extension', 'restriction'))

    @property
    def block(self):
        return get_xsd_derivation_attribute(self.elem, 'block', ('extension', 'restriction', 'substitution'))

    @property
    def substitution_group(self):
        return self.elem.get('substitutionGroup')

    def __iter__(self):
        try:
            content_iterator = self.type.content_type.iter_elements()
        except AttributeError:
            return  # It's a simple type or simple content element
        else:
            for e in content_iterator:
                yield e

    def get_attribute(self, name):
        if name[0] != '{':
            return self.type.attributes[get_qname(self.type.target_namespace, name)]
        return self.type.attributes[name]

    def iter_components(self, xsd_classes=None):
        if xsd_classes is None:
            yield self
            for obj in self.constraints.values():
                yield obj
        else:
            if isinstance(self, xsd_classes):
                yield self
            for obj in self.constraints.values():
                if isinstance(obj, xsd_classes):
                    yield obj

        if self.ref is None and not self.type.is_global:
            for obj in self.type.iter_components(xsd_classes):
                yield obj

    def iter_decode(self, elem, validation='lax', **kwargs):
        """
        Creates an iterator for decoding an Element instance.

        :param elem: The Element that has to be decoded.
        :param validation: The validation mode. Can be 'lax', 'strict' or 'skip.
        :param kwargs: Keyword arguments for the decoding process.
        :return: Yields a decoded object, eventually preceded by a sequence of \
        validation or decoding errors.
        """
        try:
            converter = kwargs['converter']
        except KeyError:
            converter = kwargs['converter'] = self.schema.get_converter(**kwargs)

        level = kwargs.pop('level', 0)
        use_defaults = kwargs.get('use_defaults', False)

        # Get the instance type: xsi:type or the schema's declaration
        if XSI_TYPE in elem.attrib:
            type_ = self.maps.lookup_type(reference_to_qname(elem.attrib[XSI_TYPE], self.namespaces))
        else:
            type_ = self.type

        # Check the xsi:nil attribute of the instance
        if validation != 'skip' and XSI_NIL in elem.attrib:
            if not self.nillable:
                yield self._validation_error("element is not nillable.", validation, elem)
            elif elem.text is not None:
                try:
                    if get_xsd_bool_attribute(elem, XSI_NIL):
                        yield self._validation_error('xsi:nil="true" but the element is not empty.', validation, elem)
                except TypeError:
                    yield self._validation_error("xsi:nil attribute must has a boolean value.", validation, elem)

        if type_.is_complex():
            if use_defaults and type_.has_simple_content():
                kwargs['default'] = self.default
            for result in type_.iter_decode(elem, validation, level=level + 1, **kwargs):
                if isinstance(result, XMLSchemaValidationError):
                    yield self._validation_error(result, validation, elem)
                else:
                    if isinstance(result[0], Decimal):
                        try:
                            element_data = ElementData(elem.tag, kwargs.get('decimal_type')(result[0]), *result[1:])
                        except TypeError:
                            element_data = ElementData(elem.tag, *result)
                    else:
                        element_data = ElementData(elem.tag, *result)
                    yield converter.element_decode(element_data, self, level)
                    del result
        else:
            # simpleType
            if not elem.attrib:
                attributes = None
            else:
                # Decode with an empty XsdAttributeGroup validator (only XML and XSD default attrs)
                for result in self.attributes.iter_decode(elem.attrib, validation, **kwargs):
                    if isinstance(result, XMLSchemaValidationError):
                        yield self._validation_error(result, validation, elem)
                    else:
                        attributes = result
                        break
                else:
                    attributes = None

            if len(elem) and validation != 'skip':
                yield self._validation_error("a simpleType element can't has child elements.", validation, elem)

            text = elem.text
            if self.fixed is not None:
                if text is None:
                    text = self.fixed
                elif text != self.fixed:
                    yield self._validation_error("must has a fixed value %r." % self.fixed, validation, elem)
            elif not text and use_defaults:
                default = self.default
                if default is not None:
                    text = default

            if text is None:
                for result in type_.iter_decode('', validation, **kwargs):
                    if isinstance(result, XMLSchemaValidationError):
                        yield self._validation_error(result, validation, elem)
                yield None
            else:
                for result in type_.iter_decode(text, validation, **kwargs):
                    if isinstance(result, XMLSchemaValidationError):
                        yield self._validation_error(result, validation, elem)
                    else:
                        if isinstance(result, Decimal):
                            try:
                                result = kwargs.get('decimal_type')(result)
                            except TypeError:
                                pass
                        element_data = ElementData(elem.tag, result, None, attributes)
                        yield converter.element_decode(element_data, self, level)
                        del result

        if validation != 'skip':
            for constraint in self.constraints.values():
                for error in constraint(elem):
                    yield self._validation_error(error, validation)

    def iter_decode_children(self, elem, validation='lax', index=0):
        """
        Creates an iterator for decoding the children of an element. Before ending the generator
        yields the last index used by inner validators.

        :param elem: The parent Element.
        :param index: Start child index, 0 for default.
        :param validation: Validation mode that can be 'strict', 'lax' or 'skip'.
        :return: Yields a sequence of values that can be tuples and/or errors and an integer at the end.
        """
        model_occurs = 0
        while True:
            try:
                child = elem[index]
            except IndexError:
                if validation != 'skip' and model_occurs == 0 and self.min_occurs > 0:
                    error = XMLSchemaChildrenValidationError(self, elem, index, self.prefixed_name)
                    yield self._validation_error(error, validation)
                yield index
                return
            else:
                tag = child.tag
                if callable(tag):
                    # When tag is a function the child is a <class 'lxml.etree._Comment'>
                    index += 1
                    continue
                elif tag == self.name:
                    yield self, child
                elif not self.qualified and tag == get_qname(self.target_namespace, self.name):
                    yield self, child
                elif self.name in self.maps.substitution_groups:
                    for e in self.schema.substitution_groups[self.name]:
                        if tag == e.name:
                            yield e, child
                            break
                    else:
                        if validation != 'skip' and model_occurs == 0 and self.min_occurs > 0:
                            error = XMLSchemaChildrenValidationError(self, elem, index, self.prefixed_name)
                            yield self._validation_error(error, validation)
                        yield index
                        return

                else:
                    if validation != 'skip' and model_occurs == 0 and self.min_occurs > 0:
                        error = XMLSchemaChildrenValidationError(self, elem, index, self.prefixed_name)
                        yield self._validation_error(error, validation)
                    yield index
                    return

            index += 1
            model_occurs += 1
            if self.max_occurs is not None and model_occurs >= self.max_occurs:
                yield index
                return

    def iter_encode(self, obj, validation='lax', **kwargs):
        """
        Creates an iterator for encoding data to an Element.

        :param obj: The data that has to be encoded.
        :param validation: The validation mode. Can be 'lax', 'strict' or 'skip'.
        :param kwargs: Keyword arguments for the encoding process.
        :return: Yields an Element, eventually preceded by a sequence of validation \
        or encoding errors.
        """
        try:
            converter = kwargs['converter']
        except KeyError:
            converter = kwargs['converter'] = self.schema.get_converter(**kwargs)

        level = kwargs.pop('level', 0)
        element_data = converter.element_encode(obj, self, level)

        try:
            type_name = element_data.attributes[XSI_TYPE]
        except (KeyError, AttributeError):
            type_ = self.type
        else:
            type_ = self.maps.lookup_type(reference_to_qname(type_name, kwargs['namespaces']))

        if type_.is_complex():
            for result in type_.iter_encode(element_data, validation, level=level + 1, **kwargs):
                if isinstance(result, XMLSchemaValidationError):
                    yield self._validation_error(result, validation, obj)
                else:
                    yield converter.etree_element(element_data.tag, *result, level=level)
                    break
            else:
                yield converter.etree_element(element_data.tag, level=level)
        else:
            # Encode a simpleType
            for result in self.attributes.iter_encode(element_data.attributes, validation, **kwargs):
                if isinstance(result, XMLSchemaValidationError):
                    yield result
                else:
                    attributes = result
                    break
            else:
                attributes = None

            if element_data.content:
                yield self._validation_error("a simpleType element can't has child elements.", validation, obj)

            if element_data.text is None:
                yield converter.etree_element(element_data.tag, attrib=attributes, level=level)
            else:
                for result in type_.iter_encode(element_data.text, validation, **kwargs):
                    if isinstance(result, XMLSchemaValidationError):
                        yield self._validation_error(result, validation, obj)
                    else:
                        yield converter.etree_element(element_data.tag, result, attrib=attributes, level=level)
                        break
                else:
                    yield converter.etree_element(element_data.tag, attrib=attributes, level=level)

        del element_data

    def is_restriction(self, other, check_particle=True):
        if isinstance(other, XsdAnyElement):
            return True  # TODO
        elif isinstance(other, XsdElement):
            if self.name != other.name:
                if other.name not in self.maps.substitution_groups:
                    return False
                else:
                    return any(self.is_restriction(e) for e in self.maps.substitution_groups[other.name])
            elif check_particle and not ParticleMixin.is_restriction(self, other):
                return False
            elif self.type is not other.type and self.type.elem is not other.type.elem and \
                    not self.type.is_derived(other.type):
                return False
            elif self.fixed != other.fixed:
                return False
            elif other.nillable is False and self.nillable:
                return False
            elif not all(value in other.block for value in self.block):
                return False
            elif not all(k in other.constraints for k in self.constraints):
                return False
        elif other.model == XSD_CHOICE_TAG:
            if ParticleMixin.is_restriction(self, other):
                return any(self.is_restriction(e, False) for e in other.iter_group())
            else:
                return any(self.is_restriction(e) for e in other.iter_group())
        else:
            match_restriction = False
            for e in other.iter_group():
                if match_restriction:
                    if not e.is_optional():
                        return False
                elif self.is_restriction(e):
                    match_restriction = True
                elif not e.is_optional():
                    return False
        return True


class Xsd11Element(XsdElement):
    """
    Class for XSD 1.1 'element' declarations.

    <element
      abstract = boolean : false
      block = (#all | List of (extension | restriction | substitution))
      default = string
      final = (#all | List of (extension | restriction))
      fixed = string
      form = (qualified | unqualified)
      id = ID
      maxOccurs = (nonNegativeInteger | unbounded)  : 1
      minOccurs = nonNegativeInteger : 1
      name = NCName
      nillable = boolean : false
      ref = QName
      substitutionGroup = List of QName
      targetNamespace = anyURI
      type = QName
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, ((simpleType | complexType)?, alternative*, (unique | key | keyref)*))
    </element>
    """
    def _parse(self):
        XsdComponent._parse(self)
        self._parse_attributes()
        index = self._parse_type()
        index = self._parse_alternatives(index)
        if self.type is None:
            if not self.alternatives:
                self.type = self.maps.lookup_type(XSD_ANY_TYPE)
        elif self.alternatives:
            self._parse_error("types alternatives incompatible with type specification.")

        self._parse_constraints(index)
        self._parse_substitution_group()

    def _parse_alternatives(self, index=0):
        self.alternatives = []
        for child in self._iterparse_components(self.elem, start=index):
            if child.tag == XSD_ALTERNATIVE_TAG:
                self.alternatives.append(XsdAlternative(child, self.schema))
                index += 1
            else:
                break
        return index

    @property
    def target_namespace(self):
        try:
            return self.elem.attrib['targetNamespace']
        except KeyError:
            return self.schema.target_namespace


class XsdAlternative(XsdComponent):
    """
    <alternative
      id = ID
      test = an XPath expression
      type = QName
      xpathDefaultNamespace = (anyURI | (##defaultNamespace | ##targetNamespace | ##local))
      {any attributes with non-schema namespace . . .}>
      Content: (annotation?, (simpleType | complexType)?)
    </alternative>
    """
    @property
    def admitted_tags(self):
        return {XSD_ELEMENT_TAG}

    @property
    def built(self):
        raise NotImplementedError
