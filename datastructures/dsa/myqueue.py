
from datastructures.dsa.myarraylist import MyArrayList


class MyQueue:
    def __init__(self):
        self.queue = MyArrayList()
        self.size = 0
        self.remove_number = 0
    def is_empty(self):
        return self.size == 0
    def add(self, item):
        self.queue.add(item)
        self.size += 1
    def remove(self):
        self.queue.removebyIndex(self.remove_number)
        self.size -= 1
        self.remove_number += 1
    @property
    def get_size(self):
        return self.size

    def clear(self):
        self.queue.my_clear()
        self.size = 0

    def peek(self):
        return self.queue.get(self.size - 1)





