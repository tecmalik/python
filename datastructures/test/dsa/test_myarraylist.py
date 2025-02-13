import unittest

from data_structures.dsa.myarraylist import MyArrayList

class MySetTest(unittest.TestCase):
    def test_if_my_array_list_is_empty(self):
        myArrayList = MyArrayList()
        self.assertTrue(myArrayList.is_empty())

    def test_if_my_array_list_is_not_empty(self):
        myArrayList = MyArrayList()
        myArrayList.add("malik")
        self.assertFalse(myArrayList.is_empty())
    def test_if_my_array_list_can_return_a_size(self):
        myArrayList = MyArrayList()
        myArrayList.add("malik")
        myArrayList.remove("malik")
        self.assertTrue(myArrayList.is_empty())
        self.assertEqual(0, myArrayList.size)
    def test_if_my_array_list_can_return_error_message_if_remove_item_not_found(self):
        myArrayList = MyArrayList()
        myArrayList.add("malik")
        myArrayList.remove("mango")
        self.assertEqual("mango not in the list",myArrayList.remove("mango"))
    def test_if_my_array_list_can_gret_items_using_index(self):
        myArrayList = MyArrayList()
        myArrayList.add("malik")
        self.assertEqual("malik", myArrayList.get(0))
    def test_if_my_array_list_can_add_x_y_and_remove_y_element(self):
        myArrayList = MyArrayList()
        myArrayList.add("malik")
        myArrayList.add("mango")
        myArrayList.remove("malik")
        self.assertEqual("mango" ,myArrayList.get(0))
    def test_if_my_array_list_can_check_if_my_list_contains_x(self):
        myArrayList = MyArrayList()
        myArrayList.add("malik")
        myArrayList.add("mango")
        self.assertTrue(myArrayList.my_contains("malik"))
    def test_if_my_array_list_can_add_g_h_i_clear_my_list(self):
        myArrayList = MyArrayList()
        myArrayList.add("malik")
        myArrayList.add("mango")
        myArrayList.add("malik2")
        self.assertEqual(None, myArrayList.my_clear())


