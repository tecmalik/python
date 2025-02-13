import unittest

from datastructures.dsa import myset
from datastructures.dsa.myset import MySet

class MySetTest(unittest.TestCase):
    def setUp(self):
        self.my_set = MySet()
    def test_if_mySet_is_empty(self):
        self.assertTrue(self.my_set.is_empty())
    def test_if_mySet_is_not_empty(self):
        self.my_set.add("1")
        self.assertFalse(self.my_set.is_empty())
    def test_if_mySet_can_contain_more_than_1_value(self):
        self.my_set.add("1")
        self.assertEqual(1, self.my_set.get_size)
        self.my_set.add("2")
        self.assertEqual(2, self.my_set.get_size)
    def test_if_my_set_wont_add_duplicate(self):
        self.my_set.add("1")
        self.my_set.add("2")
        self.my_set.add("2")
        self.assertEqual(2, self.my_set.get_size)
    def test_if_mySet_can_clear(self):
        self.my_set.add("1")
        self.my_set.add("2")
        self.my_set.my_clear()
        self.assertEqual(0 ,self.my_set.get_size)
    def test_if_mySet_can_remove_an_element(self):
        self.my_set.add("1")
        self.my_set.add("2")
        self.my_set.remove("2")
        self.assertEqual(1, self.my_set.get_size)
    def test_that_mySet_contains_an_element(self):
        self.my_set.add("1")
        self.my_set.add("2")
        self.assertTrue(self.my_set.my_contains("2"))
    def test_that_mySet_can_all_element_collection(self):
        self.my_set.add_all(["1","3","4"])
        self.assertEqual(3,self.my_set.get_size)



