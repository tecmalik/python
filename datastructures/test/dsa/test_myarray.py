import unittest
from data_structures.dsa.myarray import MyArray

class MyArrayTest(unittest.TestCase):
    def test_if_myArray_is_empty(self):
        myArray = MyArray(2)
        self.assertTrue(myArray.is_empty())
    def test_if_my_array_is_not_empty(self):
        myArray = MyArray(2)
        myArray.my_append("malik")
        self.assertFalse(myArray.is_empty())
    def test_if_myarray_has_a_size(self):
        myArray = MyArray(2)
        myArray.my_append("malik")
        self.assertEqual(2, myArray.my_length())
    def test_if_myarray_of_length_2_will_append_only_2_element(self):
        myArray = MyArray(2)
        myArray.my_append("malik")
        myArray.my_append("matin")
        myArray.my_append("hello")
        self.assertEqual(2, myArray.my_length())
        self.assertEqual("index out of bound for length 2", myArray.get(2))
    def test_if_myarray_of_length_3_will_append_2_element_and_return_3(self):
        myArray = MyArray(3)
