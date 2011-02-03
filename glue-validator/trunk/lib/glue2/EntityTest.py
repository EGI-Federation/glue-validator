#!/usr/bin/python

import re
import unittest
import glue2.data
import glue2.types

class EntityTest(unittest.TestCase):

    def __init__(self, test_name, entry):
        unittest.TestCase.__init__(self, test_name)
        self.entry = entry
        if 'dn' in entry:
            self.dn = entry['dn'][0]
        else:
            self.dn = None

        if 'objectClass' in entry:
            self.objects = entry['objectClass']
        else:
            self.objects = None

    def test_object_class(self):
        message = "The entry %s does not contain any object class" % (self.dn)
        self.assertTrue('objectClass' in self.entry , message)
        if 'objectClass' in self.entry:
            for obj in self.entry['objectClass']:
                message = "The object class %s in %s is not valid" % (obj, self.dn)
                self.assertTrue(glue2.types.is_ObjectClass(obj), message)

    def test_mandatory_attributes(self):
        """Verifying the existence of mandatory attributes."""
        for obj in self.objects:
            if obj in glue2.data.schema:
                for attribute in glue2.data.schema[obj]:
                    if glue2.data.schema[obj][attribute][2]:
                        message = "The mandatory attribute %s is not present in %s" % (attribute, self.dn)
                        self.assertTrue(attribute in self.entry, message)
        
    def test_single_valued(self):
        """Verifying single-valued attributes only have one value."""
        for obj in self.objects:
            if obj in glue2.data.schema:
                for attribute in glue2.data.schema[obj]:
                    if glue2.data.schema[obj][attribute][1]:
                        message = "The single value attribute %s has more than one value in %s" % (attribute, self.dn)
                        if attribute in self.entry:
                            self.assertEqual(len(self.entry[attribute]), 1, message)

    def test_data_types(self):
        """Validating data types."""
        for obj in self.objects:
            if obj in glue2.data.schema:
                for attribute in self.entry:
                    if attribute in glue2.data.schema[obj]:
                        data_type = glue2.data.schema[obj][attribute][0]
                        for value in self.entry[attribute]:
                            check = getattr(glue2.types, 'is_' + data_type)
                            message = "The field %s with value %s does not follow the type %s in %s" % (attribute, value, data_type, self.dn)
                            self.assertTrue(check(value), message)

if __name__ == '__main__':

    class EntityTestTest(unittest.TestCase):
        
        def setUp(self):
            self.good_entry = {
                'dn' : ['EntityId=test,o=GLUE2'],
                'objectClass' : ['GLUE2Entity'],
                'GLUE2EntityId' : ['test'],
                }
          
        def test_good_entryTest(self):
            '''Test a good entry.'''
            entry = self.good_entry
            suite = unittest.TestSuite()
            test_names = unittest.TestLoader().getTestCaseNames(EntityTest)
            for test_name in test_names:
                suite.addTest(EntityTest(test_name, entry))
            self.assertTrue(unittest.TextTestRunner().run(suite).wasSuccessful())
        def test_bad_object_class(self):
            '''Test a bad object class'''
            entry = self.good_entry
            entry['objectClass'] = ['BadObject']
            suite = unittest.TestSuite()
            test_names = unittest.TestLoader().getTestCaseNames(EntityTest)
            for test_name in test_names:
                suite.addTest(EntityTest(test_name, entry))
            self.assertFalse(unittest.TextTestRunner().run(suite).wasSuccessful())
            self.assertEqual(len(unittest.TextTestRunner().run(suite).failures),1)

    suite = unittest.TestLoader().loadTestsFromTestCase(EntityTestTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

