import unittest

from pyramid import testing

class ViewTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def test_my_view(self):
        from nodlesh.views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['project'], 'nodlesh')

class SchemaTests(unittest.TestCase):
    def setUp(self):
        from nodlesh.testers.schema import default_schema, testing_session
        self.config = testing.setUp()
        self.schema = default_schema
        self._schema = None
        self.session = testing_session()
    def tearDown(self):
        testing.tearDown()
    def _schema_restore(self):
        from nodlesh.core.db.schema import mongoalchemy_class_factory
        if self._schema is None:
            self._schema = mongoalchemy_class_factory("TestDocument", "anime", self.schema)
        return self._schema
    def test_at_restore(self):
        '''
        testing restoring functional based on custom object from another project
        '''
        self._schema_restore()
    def test_it_dump(self):
        schema = self._schema_restore()
        from nodlesh.core.db.schema import mongoalchemy_schema_factory
        mongoalchemy_schema_factory(schema)
    def test_it_counting(self):
        '''
        testing quering by resurected model
        '''
        schema = self._schema_restore()
        self.session.query(schema).count()
    def test_it_fetch_one(self):
        '''
        testing fetching from resurected model
        '''
        schema = self._schema_restore()
        self.session.query(schema).first()
        
