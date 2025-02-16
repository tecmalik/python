import unittest

from datastructures.dsa import mystack

class StackTest(unittest.TestCase):
    def setUp(self):
        self.my_stack = mystack.MyStack()
    def test_my_stack_is_empty(self):
        self.assertTrue(self.my_stack.is_empty())
    def test_my_stack_can_contain_an_element(self):
        self.my_stack.push("hello")
        self.assertFalse(self.my_stack.is_empty())
        self.assertEqual(1,self.my_stack.get_size)
    def test_my_stack_can_clear(self):
        self.my_stack.push("hello")
        self.my_stack.push("world")
        self.assertEqual(2,self.my_stack.get_size)
        self.my_stack.clear()
        self.assertEqual(0,self.my_stack.get_size)
    def test_my_stack_can_pop_element(self):
        self.my_stack.push("hello")
        self.my_stack.push("world")
        self.assertEqual("world",self.my_stack.peek())
        self.my_stack.pop()
        self.assertEqual("hello",self.my_stack.peek())

