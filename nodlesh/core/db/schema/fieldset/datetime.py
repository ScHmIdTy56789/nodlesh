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
from mongoalchemy.fields import DateTimeField

class NullableDateTimeField(DateTimeField):
    def validate_wrap(self, value):
        ''' Validates the value's type as well as it being in the valid 
            date range'''
        if value is None:
            return True
        DateTimeField.validate_wrap(self, value)