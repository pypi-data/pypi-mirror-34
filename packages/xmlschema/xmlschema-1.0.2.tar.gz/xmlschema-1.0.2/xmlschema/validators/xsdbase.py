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
This module contains base functions and classes XML Schema components.
"""
import re

from ..compat import PY3, unicode_type
from ..etree import etree_tostring, is_etree_element
from ..exceptions import XMLSchemaValueError, XMLSchemaTypeError
from ..qnames import (
    local_name, get_qname, qname_to_prefixed, XSD_ANNOTATION_TAG, XSD_APPINFO_TAG,
    XSD_DOCUMENTATION_TAG, XML_LANG, XSD_ANY_TYPE
)
from .exceptions import XMLSchemaParseError, XMLSchemaValidationError
from .parseutils import (
    get_xsd_component, iter_xsd_components, get_xsd_int_attribute, get_xpath_default_namespace_attribute
)

XSD_VALIDATION_MODES = {'strict', 'lax', 'skip'}
"""
XML Schema validation modes
Ref.: https://www.w3.org/TR/xmlschema11-1/#key-va
"""


class XsdBaseComponent(object):
    """
    Common base class for representing XML Schema components. A concrete XSD component have
    to report its validity collecting building errors and implementing the properties.

    See: https://www.w3.org/TR/xmlschema-ref/

    :param validation: Defines the XSD validation mode to use for build the schema, \
    it's value can be 'strict', 'lax' or 'skip'.
    :type validation: str
    """
    def __init__(self, validation='strict'):
        if validation not in XSD_VALIDATION_MODES:
            raise XMLSchemaValueError("validation argument can be 'strict', 'lax' or 'skip': %r" % validation)
        self.validation = validation
        self.errors = []  # component errors

    def __str__(self):
        # noinspection PyCompatibility,PyUnresolvedReferences
        return unicode(self).encode("utf-8")

    def __unicode__(self):
        return self.__repr__()

    if PY3:
        __str__ = __unicode__

    def _parse(self):
        if self.errors:
            del self.errors[:]

    def _parse_error(self, error, elem=None):
        if self.validation == 'skip':
            return

        elem = elem if elem is not None else getattr(self, 'elem', None)
        if isinstance(error, XMLSchemaParseError):
            error.component = self
            error.elem = elem
        else:
            error = XMLSchemaParseError(str(error), self, elem)

        if self.validation == 'lax':
            self.errors.append(error)
        else:
            raise error

    def _parse_xpath_default_namespace(self, elem, namespaces, target_namespace, default=None):
        try:
            xpath_default_namespace = get_xpath_default_namespace_attribute(elem)
        except XMLSchemaValueError as error:
            self._parse_error(error, elem)
            self._xpath_default_namespace = namespaces['']
        else:
            if xpath_default_namespace == '##local':
                self._xpath_default_namespace = ''
            elif xpath_default_namespace == '##defaultNamespace':
                self._xpath_default_namespace = namespaces['']
            elif xpath_default_namespace == '##targetNamespace':
                self._xpath_default_namespace = target_namespace
            elif xpath_default_namespace is not None:
                self._xpath_default_namespace = xpath_default_namespace
            elif default is not None:
                self._xpath_default_namespace = default

    @property
    def built(self):
        """
        Property that is ``True`` if schema component has been fully parsed and built, ``False`` otherwise.
        """
        raise NotImplementedError

    @property
    def validation_attempted(self):
        """
        Property that returns the XSD component validation status. It can be
        'full', 'partial' or 'none'.

        | https://www.w3.org/TR/xmlschema-1/#e-validation_attempted
        | https://www.w3.org/TR/2012/REC-xmlschema11-1-20120405/#e-validation_attempted
        """
        raise NotImplementedError

    @property
    def validity(self):
        """
        Property that returns the XSD component validity. It can be ‘valid’, ‘invalid’ or ‘notKnown’.

        | https://www.w3.org/TR/xmlschema-1/#e-validity
        | https://www.w3.org/TR/2012/REC-xmlschema11-1-20120405/#e-validity
        """
        if self.errors or any([comp.errors for comp in self.iter_components()]):
            return 'invalid'
        elif self.built:
            return 'valid'
        else:
            return 'notKnown'

    def iter_components(self, xsd_classes=None):
        """
        Returns an iterator for traversing all descendant XSD components.

        :param xsd_classes: Returns only a specific class/classes of components, \
        otherwise returns all components.
        """
        raise NotImplementedError

    @property
    def all_errors(self):
        """
        A list with the errors of the XSD component and of its descendants.
        """
        errors = []
        for comp in self.iter_components():
            if comp.errors:
                errors.extend(comp.errors)
        return errors


class XsdComponent(XsdBaseComponent):
    """
    Class for schema components.

    :param elem: ElementTree's node containing the definition.
    :param schema: The XMLSchema object that owns the definition.
    :param name: Name of the component, maybe overwritten by the parse of the `elem` argument.
    :param is_global: `True` if the instance is a global component, `False` if it's local.
    """
    _REGEX_SPACE = re.compile(r'\s')
    _REGEX_SPACES = re.compile(r'\s+')

    qualified = True  # For name matching, unqualified matching may be admitted only for elements and attributes.

    def __init__(self, elem, schema, name=None, is_global=False):
        super(XsdComponent, self).__init__(schema.validation)
        if name == '':
            raise XMLSchemaValueError("'name' cannot be an empty string!")
        self.is_global = is_global
        self.name = name
        self.schema = schema
        self.elem = elem

    def __setattr__(self, name, value):
        if name == "elem":
            if not is_etree_element(value):
                raise XMLSchemaTypeError("%r attribute must be an Etree Element: %r" % (name, value))
            elif value.tag not in self.admitted_tags:
                raise XMLSchemaValueError(
                    "wrong XSD element %r for %r, must be one of %r." % (
                        local_name(value.tag), self,
                        [local_name(tag) for tag in self.admitted_tags]
                    )
                )
            elif hasattr(self, 'elem'):
                self._elem = self.elem  # redefinition cases
            super(XsdComponent, self).__setattr__(name, value)
            self._parse()
            return
        elif name == "schema":
            if hasattr(self, 'schema') and self.schema.target_namespace != value.target_namespace:
                raise XMLSchemaValueError(
                    "cannot change 'schema' attribute of %r: the actual %r has a different "
                    "target namespace than %r." % (self, self.schema, value)
                )
        super(XsdComponent, self).__setattr__(name, value)

    @property
    def target_namespace(self):
        return self.schema.target_namespace

    @property
    def namespaces(self):
        return self.schema.namespaces

    @property
    def xpath_default_namespace(self):
        try:
            return self._xpath_default_namespace
        except AttributeError:
            getattr(self.schema, '_xpath_default_namespace', None)

    @property
    def maps(self):
        return self.schema.maps

    def __repr__(self):
        if self.name is None:
            return u"<%s at %#x>" % (self.__class__.__name__, id(self))
        else:
            return u'%s(name=%r)' % (self.__class__.__name__, self.prefixed_name)

    def _validation_error(self, error, validation, obj=None):
        if validation == 'skip':
            raise XMLSchemaValueError("'skip' validation mode incompatible with error handling.")
        elif not isinstance(error, XMLSchemaValidationError):
            error = XMLSchemaValidationError(self, obj, reason=unicode_type(error))
        elif obj and error.elem is None and is_etree_element(obj):
            error.elem = obj

        if validation == 'strict':
            raise error
        else:
            return error

    def _parse(self):
        super(XsdComponent, self)._parse()
        try:
            if self.elem[0].tag == XSD_ANNOTATION_TAG:
                self.annotation = XsdAnnotation(self.elem[0], self.schema)
            else:
                self.annotation = None
        except (TypeError, IndexError):
            self.annotation = None

    def _parse_component(self, elem, required=True, strict=True):
        try:
            return get_xsd_component(elem, required, strict)
        except XMLSchemaValueError as err:
            self._parse_error(str(err), elem)

    def _iterparse_components(self, elem, start=0):
        try:
            for obj in iter_xsd_components(elem, start):
                yield obj
        except XMLSchemaValueError as err:
            self._parse_error(str(err), elem)

    def _parse_properties(self, *properties):
        for name in properties:
            try:
                getattr(self, name)
            except (ValueError, TypeError) as err:
                self._parse_error(str(err))

    @property
    def local_name(self):
        return local_name(self.name)

    @property
    def qualified_name(self):
        return get_qname(self.target_namespace, self.name)

    @property
    def prefixed_name(self):
        return qname_to_prefixed(self.name, self.namespaces)

    @property
    def id(self):
        """The ``'id'`` attribute of the component tag, ``None`` if missing."""
        return self.elem.get('id')

    @property
    def validation_attempted(self):
        return 'full' if self.built else 'partial'

    @property
    def built(self):
        raise NotImplementedError

    @property
    def admitted_tags(self):
        raise NotImplementedError

    def match(self, name, default_namespace=None):
        """Matching method for component name."""
        if not name or name[0] == '{':
            return self.name == name
        elif default_namespace:
            qname = '{%s}%s' % (default_namespace, name)
            return self.name == name or self.name == qname or not self.qualified and self.local_name == name
        else:
            return self.name == name or not self.qualified and self.local_name == name

    def iter_components(self, xsd_classes=None):
        """Creates an iterator for XSD subcomponents."""
        if xsd_classes is None or isinstance(self, xsd_classes):
            yield self

    def to_string(self, indent='', max_lines=None, spaces_for_tab=4):
        """
        Returns the XML elements that declare or define the component as a string.
        """
        if self.elem is not None:
            return etree_tostring(self.elem, indent, max_lines, spaces_for_tab)
        else:
            return str(None)


class XsdAnnotation(XsdComponent):
    """
    Class for XSD 'annotation' definitions.

    <annotation
      id = ID
      {any attributes with non-schema namespace . . .}>
      Content: (appinfo | documentation)*
    </annotation>

    <appinfo
      source = anyURI
      {any attributes with non-schema namespace . . .}>
      Content: ({any})*
    </appinfo>

    <documentation
      source = anyURI
      xml:lang = language
      {any attributes with non-schema namespace . . .}>
      Content: ({any})*
    </documentation>
    """

    @property
    def admitted_tags(self):
        return {XSD_ANNOTATION_TAG}

    @property
    def built(self):
        return True

    def _parse(self):
        super(XsdComponent, self)._parse()  # Skip parent class method (that parses also annotations)
        self.appinfo = []
        self.documentation = []
        for child in self.elem:
            if child.tag == XSD_APPINFO_TAG:
                for key in child.attrib:
                    if key != 'source':
                        self._parse_error("wrong attribute %r for appinfo declaration." % key)
                self.appinfo.append(child)
            elif child.tag == XSD_DOCUMENTATION_TAG:
                for key in child.attrib:
                    if key not in ['source', XML_LANG]:
                        self._parse_error("wrong attribute %r for documentation declaration." % key)
                self.documentation.append(child)


class XsdType(XsdComponent):

    base_type = None
    derivation = None

    @property
    def built(self):
        raise NotImplementedError

    @property
    def admitted_tags(self):
        raise NotImplementedError

    @staticmethod
    def is_simple():
        raise NotImplementedError

    @staticmethod
    def is_complex():
        raise NotImplementedError

    @staticmethod
    def is_atomic():
        return None

    def is_empty(self):
        raise NotImplementedError

    def is_emptiable(self):
        raise NotImplementedError

    def has_simple_content(self):
        raise NotImplementedError

    def has_mixed_content(self):
        raise NotImplementedError

    def is_element_only(self):
        raise NotImplementedError

    @property
    def content_type_label(self):
        if self.is_empty():
            return 'empty'
        elif self.has_simple_content():
            return 'simple'
        elif self.is_element_only():
            return 'element-only'
        elif self.has_mixed_content():
            return 'mixed'
        else:
            return 'unknown'

    def is_derived(self, other, derivation=None):
        if other.name == XSD_ANY_TYPE or self.base_type == other:
            return True if derivation is None else derivation == self.derivation
        elif self.base_type is not None:
            return self.base_type.is_derived(other, derivation)
        else:
            return False

    def is_subtype(self, qname):
        if qname == XSD_ANY_TYPE or self.name == qname:
            return True
        elif self.base_type is not None:
            return self.base_type.is_subtype(qname)
        else:
            return False


class XsdDeclaration(XsdComponent):

    def __repr__(self):
        if self.ref is None:
            return u'%s(name=%r)' % (self.__class__.__name__, self.prefixed_name)
        else:
            return u'%s(ref=%r)' % (self.__class__.__name__, self.prefixed_name)

    @property
    def ref(self):
        return self.elem.get('ref')

    @property
    def built(self):
        raise NotImplementedError

    @property
    def admitted_tags(self):
        raise NotImplementedError


class ParticleMixin(object):
    """
    Mixin for objects related to XSD Particle Schema Components:

      https://www.w3.org/TR/2012/REC-xmlschema11-1-20120405/structures.html#p
      https://www.w3.org/TR/2012/REC-xmlschema11-1-20120405/structures.html#t
    """

    def _parse_particle(self):
        max_occurs = self.max_occurs
        if max_occurs is not None and self.min_occurs > max_occurs:
            getattr(self, '_parse_error')(
                "maxOccurs must be 'unbounded' or greater than minOccurs:"
            )

    @property
    def min_occurs(self):
        return get_xsd_int_attribute(getattr(self, 'elem'), 'minOccurs', default=1, minimum=0)

    @property
    def max_occurs(self):
        try:
            return get_xsd_int_attribute(getattr(self, 'elem'), 'maxOccurs', default=1, minimum=0)
        except (TypeError, ValueError):
            if getattr(self, 'elem').attrib['maxOccurs'] == 'unbounded':
                return None
            raise

    def is_optional(self):
        return getattr(self, 'elem').get('minOccurs', '').strip() == "0"

    def is_emptiable(self):
        return self.min_occurs == 0

    def is_single(self):
        return self.max_occurs == 1

    def is_restriction(self, other):
        if self.min_occurs < other.min_occurs:
            return False
        if other.max_occurs is not None:
            if self.max_occurs is None:
                return False
            elif self.max_occurs > other.max_occurs:
                return False
        return True


class ValidatorMixin(object):
    """
    Mixin for implementing XML Schema validators. A derived class must implement the
    methods `iter_decode` and `iter_encode`.
    """
    def validate(self, source, use_defaults=True):
        """
        Validates an XML data against the XSD schema/component instance.

        :param source: the source of XML data. For a schema can be a path \
        to a file or an URI of a resource or an opened file-like object or an Element Tree \
        instance or a string containing XML data. For other XSD components can be a string \
        for an attribute or a simple type validators, or an ElementTree's Element otherwise.
        :param use_defaults: indicates whether to use default values for filling missing data.
        :raises: :exc:`XMLSchemaValidationError` if XML *data* instance is not a valid.
        """
        for error in self.iter_errors(source, use_defaults=use_defaults):
            raise error

    def iter_errors(self, source, path=None, use_defaults=True):
        """
        Creates an iterator for the errors generated by the validation of an XML data
        against the XSD schema/component instance.

        :param source: the source of XML data. For a schema can be a path \
        to a file or an URI of a resource or an opened file-like object or an Element Tree \
        instance or a string containing XML data. For other XSD components can be a string \
        for an attribute or a simple type validators, or an ElementTree's Element otherwise.
        :param path: is an optional XPath expression that defines the parts of the document \
        that have to be validated. The XPath expression considers the schema as the root element \
        with global elements as its children.
        :param use_defaults: Use schema's default values for filling missing data.
        """
        for result in self.iter_decode(source, path, use_defaults=use_defaults):
            if isinstance(result, XMLSchemaValidationError):
                yield result
            else:
                del result

    def is_valid(self, source, use_defaults=True):
        """
        Like :meth:`validate` except that do not raises an exception but returns
        ``True`` if the XML document is valid, ``False`` if it's invalid.
        """
        error = next(self.iter_errors(source, use_defaults=use_defaults), None)
        return error is None

    def decode(self, source, *args, **kwargs):
        """
        Decodes XML data using the XSD schema/component.

        :param source: the source of XML data. For a schema can be a path to a file or an \
        URI of a resource or an opened file-like object or an Element Tree \
        instance or a string containing XML data. For other XSD components can be a string \
        for an attribute or a simple type validators, or an ElementTree's Element otherwise.
        :param args: arguments that maybe passed to :func:`XMLSchema.iter_decode`.
        :param kwargs: keyword arguments from the ones included in the optional \
        arguments of the :func:`XMLSchema.iter_decode`.
        :return: a dictionary like object if the XSD component is an element, a \
        group or a complex type; a list if the XSD component is an attribute group; \
         a simple data type object otherwise. If *validation* argument is 'lax' a 2-items \
        tuple is returned, where the first item is the decoded object and the second item \
        is a list containing the errors.
        :raises: :exc:`XMLSchemaValidationError` if the object is not decodable by \
        the XSD component, or also if it's invalid when ``validation='strict'`` is provided.
        """
        validation = kwargs.pop('validation', 'strict')
        if validation not in XSD_VALIDATION_MODES:
            raise XMLSchemaValueError("validation argument can be 'strict', 'lax' or 'skip': %r" % validation)
        errors = []

        for result in self.iter_decode(source, validation=validation, *args, **kwargs):
            if isinstance(result, XMLSchemaValidationError):
                if validation == 'strict':
                    raise result
                elif validation == 'lax':
                    errors.append(result)
            elif validation == 'lax':
                return result, errors
            else:
                return result
    to_dict = decode

    def encode(self, obj, *args, **kwargs):
        """
        Encodes data to XML using the XSD schema/component.

        :param obj: the data to be encoded to XML.
        :param args: arguments that maybe passed to :func:`XMLSchema.iter_encode`.
        :param kwargs: keyword arguments from the ones included in the optional \
        arguments of the :func:`XMLSchema.iter_encode`.
        :return: An element tree's Element if the original data is a structured data or \
        a string if it's simple type datum. If *validation* argument is 'lax' a 2-items \
        tuple is returned, where the first item is the encoded object and the second item \
        is a list containing the errors.
        :raises: :exc:`XMLSchemaValidationError` if the object is not encodable by \
        the XSD component, or also if it's invalid when ``validation='strict'`` is provided.
        """
        validation = kwargs.pop('validation', 'strict')
        if validation not in XSD_VALIDATION_MODES:
            raise XMLSchemaValueError("validation argument can be 'strict', 'lax' or 'skip': %r" % validation)
        errors = []

        for result in self.iter_encode(obj, validation=validation, *args, **kwargs):
            if isinstance(result, XMLSchemaValidationError):
                if validation == 'strict':
                    raise result
                elif validation == 'lax':
                    errors.append(result)
            elif validation == 'lax':
                return result, errors
            else:
                return result
    to_etree = encode

    def iter_decode(self, source, validation='lax', *args, **kwargs):
        """
        Creates an iterator for decoding an XML source to a Python object.

        :param source: the XML data source. The argument type depends by implementation.
        :param validation: the validation mode. Can be 'lax', 'strict' or 'skip.
        :param args: additional arguments for the decoder API.
        :param kwargs: keyword arguments for the decoder API.
        :return: Yields a decoded object, eventually preceded by a sequence of \
        validation or decoding errors.
        """
        raise NotImplementedError

    def iter_encode(self, obj, validation='lax', *args, **kwargs):
        """
        Creates an iterator for Encode data to an Element.

        :param obj: The data that has to be encoded.
        :param validation: The validation mode. Can be 'lax', 'strict' or 'skip'.
        :param args: additional arguments for the encoder API.
        :param kwargs: keyword arguments for the encoder API.
        :return: Yields an Element, eventually preceded by a sequence of validation \
        or encoding errors.
        """
        raise NotImplementedError
