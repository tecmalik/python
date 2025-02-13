import unittest
from datastructures.dsa.myarray import MyArray

class MyArrayTest(unittest.TestCase):
    def test_if_myArray_is_empty(self):
        my_array = MyArray(2)
        self.assertTrue(my_array.is_empty())
    def test_if_my_array_is_not_empty(self):
        my_array  = MyArray(2)
        my_array.my_append("malik")
        self.assertFalse(my_array.is_empty())
    def test_if_my_array_has_a_size(self):
        my_array = MyArray(2)
        my_array.my_append("malik")
        self.assertEqual(2, my_array.my_length())
    def test_if_my_array_of_length_2_will_append_only_2_element(self):
        my_array = MyArray(2)
        my_array.my_append("malik")
        my_array.my_append("matin")
        my_array.my_append("hello")
        self.assertEqual(2, my_array.my_length())
        self.assertEqual("index out of bound for length 2", my_array.get(2))
    def test_if_my_array_of_length_3_will_append_only_3_element(self):
        my_array = MyArray(3)
        my_array.my_append("malik")
        my_array.my_append("matin")
        my_array.my_append("hello")
        self.assertEqual(3, my_array.my_length())
    def test_i_can_return_its_length(self):
        my_array = MyArray(2)
        my_array.my_append("malik")
        self.assertEqual(2, my_array.my_length())


