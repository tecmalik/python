import unittest

from datastructures.dsa import myqueue

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.my_queue = myqueue.MyQueue()
    def test_my_queue_is_empty(self):
        self.assertTrue(self.my_queue.is_empty())
    def test_my_queue_can_contain_an_element(self):
        self.my_queue.add("hello")
        self.assertFalse(self.my_queue.is_empty())
        self.assertEqual(1,self.my_queue.get_size)
    def test_my_queue_can_clear(self):
        self.my_queue.add("hello")
        self.my_queue.add("world")
        self.assertEqual(2,self.my_queue.get_size)
        self.my_queue.clear()
        self.assertEqual(0,self.my_queue.get_size)
    def test_my_queue_can_pop_element(self):
        self.my_queue.add("hello")
        self.my_queue.add("world")
        self.assertEqual("world",self.my_queue.peek())





