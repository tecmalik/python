import unittest
from data_structures.myarray import MyArray

class MyArrayTest(unittest.TestCase):
    def test_if_myArray_is_empty(self):
        myArray = MyArray(2)
        self.assertTrue(myArray.isempty())
    def test_if_my_array_is_not_empty(self):
        myArray = MyArray(2)
        myArray.myappend("malik")
        self.assertFalse(myArray.isempty())
    def test_if_myarray_has_a_size(self):
        myArray = MyArray(2)
        myArray.myappend("malik")
        self.assertEqual(2 ,myArray.mylength())
    def test_if_myarray_of_length_2_will_append_only_2_element(self):
        myArray = MyArray(2)
        myArray.myappend("malik")
        myArray.myappend("matin")
        myArray.myappend("hello")
        self.assertEqual(2, myArray.mylength())
        self.assertEqual("index out of bound for length 2", myArray.get(2))
    def test_if_myarray_of_length_3_will_append_2_element_and_return_3(self):
        myArray = MyArray(3)
