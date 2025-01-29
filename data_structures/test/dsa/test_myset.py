import unittest

from data_structures.dsa.myset import MySet

class MySetTest(unittest.TestCase):
    def test_if_mySet_is_empty(self):
        mySet = MySet()
        self.assertTrue(mySet.is_empty())
    def test_if_mySet_is_not_empty(self):
        mySet = MySet()
        mySet.add("1")
        self.assertFalse(mySet.is_empty())
    def test_if_mySet_can_contain_more_value(self):
        """    self.assertFalse(mySet.is_empty()):
    def test_if_mySet_can_add_an_elament(self):
        MySet = MySet()
        MySet.myadd("malik")
"""
