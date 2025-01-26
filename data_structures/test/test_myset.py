import unittest

from data_structures.myset import MySet

class MySetTest(unittest.TestCase):
    def test_if_myset_is_empty(self):
        mySet = MySet(2)
        self.assertTrue(mySet.isempty())
    def test_if_myset_is_not_empty(self):
        mySet = MySet(2)
        mySet.myadd("malik")
        self.assertFalse(mySet.isempty())
