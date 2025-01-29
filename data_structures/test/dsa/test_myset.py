import unittest

from data_structures.dsa import myset
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
        mySet = MySet()
        mySet.add("1")
        mySet.add("2")
        self.assertEqual(0, mySet.get_size())
    def test_if_myset_wont_add_duplicate(self):
        mySet = MySet()
        mySet.add("1")
        mySet.add("2")
        mySet.add("2")
        self.assertEqual(2, mySet.get_size())
    def test_if_mySet_can_clear(self):
        mySet = MySet()
        mySet.add("1")
        mySet.add("2")
        mySet.my_clear()
        self.assertEqual(0 ,mySet.get_size())
    def test_if_mySet_can_remove_an_element(self):
        mySet = MySet()
        mySet.add("1")
        mySet.add("2")
        mySet.remove("2")
        self.assertEqual(1, mySet.get_size())
    def test_if_mySet_contains_an_element(self):
        mySet = MySet()
        mySet.add("1")
        mySet.add("2")
        assertTrue(myset.my_contains("2"))


