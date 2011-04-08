'''
Created on Apr 8, 2011

@author: bstar
'''
from mongoalchemy.fields import DateTimeField

class NullableDateTimeField(DateTimeField):
    def validate_wrap(self, value):
        ''' Validates the value's type as well as it being in the valid 
            date range'''
        if value is None:
            return True
        DateTimeField.validate_wrap(self, value)