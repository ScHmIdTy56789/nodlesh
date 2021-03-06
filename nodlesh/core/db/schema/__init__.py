'''
This file is part of nodlesh.

    nodlesh is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    nodlesh is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with nodlesh.  If not, see <http://www.gnu.org/licenses/>.
'''
import colander
import datetime
from mongoalchemy import fields
from nodlesh.core.db.schema.fieldset import NullableDateTimeField
from mongoalchemy.document import Document

colander_data_types = {
    'int': colander.Integer,
    'string': colander.String,
    'map': colander.Mapping,
    'tuple': colander.Tuple,
    'sequence': colander.Sequence,
    'float': colander.Float,
    'decimal': colander.Decimal,
    'bool': colander.Boolean,
    'datetime': colander.DateTime,
    
}

funcs_schema = {
               'datetime.datetime.now': datetime.datetime.now
               }
innered_data_types = 'list', 'tuple', 'sequence', 'dict', 'set',

mongoalchemy_data_types = {
                           "string": fields.StringField,
                           "int": fields.IntField,
                           'datetime': NullableDateTimeField,
                           'sequence': fields.SequenceField,
                           'list': fields.ListField,
                           'float': fields.FloatField,
                           'tuple': fields.TupleField,
                           'bool': fields.BoolField,
                           'binary': fields.BinaryField,
                           'dict': fields.DictField,
                           'number': fields.NumberField,
                           'object_id': fields.ObjectIdField,
                           'set': fields.SetField,
                           }
mongoalchemy_fields_kwargs = ['default', 'required', 'min_date', 'max_date', 'min_value', 'max_value', 'min_capacity', 'max_capacity', 'max_length', 'min_length' ] 
def mongoalchemy_get_classtypes():
    result = {}
    for el_type, el_class in mongoalchemy_data_types.iteritems():
        result[el_class.__name__] = el_type
    return result
def mongoalchemy_field_schema_factory(field, classtypes):
    result = {}
    f_type = classtypes[field.__class__.__name__]
    result['type'] = f_type
    result['name'] = field.db_field
    if f_type in innered_data_types:
        result['inner'] = mongoalchemy_field_schema_factory(field.item_type, classtypes)
    args = {}
    for el in mongoalchemy_fields_kwargs:
        if hasattr(field, el): 
            args[el] = getattr(field, el)
    result['args'] = args    
    return result
def mongoalchemy_schema_factory(mongoalchemy_class):
    classtypes = mongoalchemy_get_classtypes()
    result = {}
    for field in mongoalchemy_class.get_fields().values():
        field_schema = mongoalchemy_field_schema_factory(field, classtypes)
        result[field.name] = field_schema
    return result
def mongoalchemy_field_factory(schema_field):
    field = None
    el_type =schema_field['type']
    if el_type == 'list':
        field = mongoalchemy_data_types[schema_field['type']](mongoalchemy_field_factory(schema_field['inner']),**schema_field['args'])
    else:
        field = mongoalchemy_data_types[schema_field['type']](**schema_field['args'])
    return field
def mongoalchemy_class_factory(class_name, collection_name, attrs):
    newattrs = {}
    for el_key, el_value in attrs.iteritems():
        field = mongoalchemy_field_factory(el_value)
        newattrs[el_key] = field
    cls = type(class_name, (Document,), newattrs)
    cls.config_collection_name = collection_name
    return cls
