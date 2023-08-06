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
This subpackage contains classes and constants for XML Schema components.
"""
from .xsdbase import (
    XsdBaseComponent, XsdComponent, XsdDeclaration, XsdAnnotation, XsdType, ParticleMixin, ValidatorMixin
)
from .constraints import XsdSelector, XsdFieldSelector, XsdConstraint, XsdKeyref, XsdKey, XsdUnique
from .notations import XsdNotation
from .wildcards import XsdAnyElement, XsdAnyAttribute
from .attributes import XsdAttribute, XsdAnyAttribute, XsdAttributeGroup
from .simple_types import (
    xsd_simple_type_factory, XsdSimpleType, XsdAtomic, XsdAtomicBuiltin,
    XsdAtomicRestriction, XsdList, XsdUnion
)
from .complex_types import XsdComplexType
from .groups import XsdGroup
from .elements import XsdElement
from .facets import (
    XSD_10_FACETS, XSD_11_FACETS, STRING_FACETS, BOOLEAN_FACETS, FLOAT_FACETS,
    DECIMAL_FACETS, DATETIME_FACETS, XsdSingleFacet, XsdPatternsFacet, XsdEnumerationFacet
)
from .builtins import xsd_builtin_types_factory, xsd_build_any_attribute_group, xsd_build_any_content_group
from .globals_ import XsdGlobals
from .schema import XMLSchemaMeta, XMLSchemaBase, XMLSchema, XMLSchema10
