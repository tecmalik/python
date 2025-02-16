import unittest

from datastructures.dsa.myarraylist import MyArrayList

class MySetTest(unittest.TestCase):
    def setUp(self):
        self.my_array_list = MyArrayList()
    def test_if_my_array_list_is_empty(self):
        self.assertTrue(self.my_array_list.is_empty())

    def test_if_my_array_list_is_not_empty(self):
        self.my_array_list.add("malik")
        self.assertFalse(self.my_array_list.is_empty())
    def test_if_my_array_list_can_return_a_size(self):
        self.my_array_list.add("malik")
        self.my_array_list.remove("malik")
        self.assertTrue(self.my_array_list.is_empty())
        self.assertEqual(0, self.my_array_list.size)
    def test_if_my_array_list_can_return_error_message_if_remove_item_not_found(self):
        self.my_array_list.add("malik")
        self.my_array_list.remove("mango")
        self.assertEqual("mango not in the list",self.my_array_list.remove("mango"))
    def test_if_my_array_list_can_gret_items_using_index(self):
        self.my_array_list.add("malik")
        self.assertEqual("malik", self.my_array_list.get(0))
    def test_if_my_array_list_can_add_x_y_and_remove_y_element(self):
        self.my_array_list.add("malik")
        self.my_array_list.add("mango")
        self.my_array_list.remove("malik")
        self.assertEqual("mango" ,self.my_array_list.get(0))
    def test_if_my_array_list_can_check_if_my_list_contains_x(self):
        self.my_array_list.add("malik")
        self.my_array_list.add("mango")
        self.assertTrue(self.my_array_list.my_contains("malik"))
    def test_if_my_array_list_can_add_g_h_i_clear_my_list(self):
        self.my_array_list.add("malik")
        self.my_array_list.add("mango")
        self.my_array_list.add("malik2")
        self.assertEqual(None, self.my_array_list.my_clear())
    def test_that_i_can_insert_to_a_particula_index(self):
        self.my_array_list.add("malik")
        self.my_array_list.add("mango")
        self.my_array_list.insert(0,"malik3")
        self.assertEqual("malik3", self.my_array_list.get(0))


