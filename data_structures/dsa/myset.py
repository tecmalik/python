from data_structures.dsa.myarraylist import MyArrayList


class MySet:
    def __init__(self):
        self.set = MyArrayList()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, value:str):
        if(self.set.myContains(value) == False):
            self.set.add(value)
            self.size += 1

    def get_size(self):
        return self.size

    def my_clear(self):
        self.size = 0
        self.set.my_clear()

    def remove(self, element:str):
        self.set.remove(element)
        self.size -= 1
    def my_contains(element):
        container = id
        return container.my_contains(element)
    def my_contains(self):
        return None