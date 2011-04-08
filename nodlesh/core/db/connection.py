'''
Created on 07.04.2011

@author: bstar
'''
from pymongo import Connection
from pyramid.events import NewRequest
DB_IGNORE = set('system.index')
DB_SCHEME = 'nodlesh_scheme'

def wrap_mongo_session(event):
    settings = event.request.registry.settings
    db = settings['mongo_conn']
    event.request.db = db

def generate_schema(session):
    '''
    '''

def create_mongo_session(config, settings):
    mongo_connection = Connection(host=settings['mongo.host'], port=int(settings['mongo.port']))
    mongo_session = getattr(mongo_connection, settings['mongo.database'])
    config.registry.settings['mongo_conn'] = mongo_session
    config.add_subscriber(wrap_mongo_session, NewRequest)
    return mongo_session