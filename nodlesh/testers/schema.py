import unittest
from pyramid import testing

from mongoalchemy.session import Session
def testing_session():
    return Session.connect("nonechan_com")

default_schema = {
    "type":{ 
            "type": "string", 
            "args": {"max_length": 50, "default": "TV", "required": True}
            },
    'title': {
              'type': 'string',
              'args': {'max_length': 200, 'required': True}
              },
    'episodes': {
                 'type': 'int',
                 'args': {'default': None}
                 },
    'status': {
               'type': 'string',
               'args': {'max_length': 100, 'default': 'Finished Airing', 'required': True}
               },
    'aired_start': {
                    'type': 'datetime',
                    'args': {'default': None}
                    },
    'aired_ended': {
                    'type': 'datetime',
                    'args': {'default': None}
                    },
    'duration': {
                 'type': 'string',
                 'args': {'max_length': 200, 'default': ''}
                 },
    'adult_rating': {
                     'type': 'string',
                     'args': {
                              'max_length': 200, 
                              'default': ''
                              }
                     },
    'synopsis': {
                 'type': 'string',
                 'args': {
                          'default': ''
                          }
                 },
    'usertags': {
                 'type': 'list',
                 'args': {'default': []},
                 'inner': {
                           'type': 'string',
                           'args': {'max_length': 100,}
                           } 
                 },
    'created': {
                'type': 'datetime',
                'args': {'default': 'datetime.datetime.now'}
                },
    'modified': {
                'type': 'datetime',
                'args': {'default': 'datetime.datetime.now'}
                },
    'related_adaptation': {
                           'type': 'list',
                           'args': {'default': []},
                           'inner': {
                                     'type': 'object_id',
                                     'args': {},
                                     } 
                           },
    'related_side_story': {
                           'type': 'list',
                           'args': {'default': []},
                           'inner': {
                                     'type': 'object_id',
                                     'args': {},
                                     } 
                           },
    'related_alternative_version': {
                           'type': 'list',
                           'args': {'default': []},
                           'inner': {
                                     'type': 'object_id',
                                     'args': {},
                                     } 
                           },
    'related_sequel': {
                           'type': 'list',
                           'args': {'default': []},
                           'inner': {
                                     'type': 'object_id',
                                     'args': {},
                                     } 
                           },
    'related_prequel': {
                           'type': 'list',
                           'args': {'default': []},
                           'inner': {
                                     'type': 'object_id',
                                     'args': {},
                                     } 
                           },
    'related_summary': {
                           'type': 'list',
                           'args': {'default': []},
                           'inner': {
                                     'type': 'object_id',
                                     'args': {},
                                     } 
                           },
    'characters': {
                           'type': 'list',
                           'args': {'default': []},
                           'inner': {
                                     'type': 'object_id',
                                     'args': {},
                                     } 
                           },
    'actors': {
                           'type': 'list',
                           'args': {'default': []},
                           'inner': {
                                     'type': 'object_id',
                                     'args': {},
                                     } 
                           },
    'usertags': {
                           'type': 'list',
                           'args': {'default': []},
                           'inner': {
                                     'type': 'string',
                                     'args': {"max_length": 200},
                                     } 
                           },
    'genres': {
                           'type': 'list',
                           'args': {'default': []},
                           'inner': {
                                     'type': 'string',
                                     'args': {"max_length": 100},
                                     } 
                           },
}