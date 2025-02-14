from datastructures.dsa.myarraylist import MyArrayList

class MyStack:
    def __init__(self):
        self.my_stack = MyArrayList()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, item):
        self.my_stack.add(item)
        self.size += 1

    def remove(self, item):
        self.my_stack.remove(item)

    @property
    def get_size(self):
        return self.size

    def clear(self):
        self.my_stack.my_clear()
        self.size = 0

    def peek(self):
        return self.my_stack.get(self.size - 1)

    def poll(self,):
        item = self.my_stack.get();
