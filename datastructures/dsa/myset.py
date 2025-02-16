from datastructures.dsa.myarraylist import MyArrayList


class MySet:
    def __init__(self):
        self.set = MyArrayList()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, value:str):
        if(self.set.my_contains(value) == False):
            self.set.add(value)
            self.size += 1

    @property
    def get_size(self):
        return self.size

    def my_clear(self):
        self.size = 0
        self.set.my_clear()

    def remove(self, element:str):
        self.set.remove(element)
        self.size -= 1
    def my_contains(self, element):
        return self.set.my_contains(element)

    def add_all(self, *elements):
        for element in elements:
            self.set.add(element)
            self.size += 1

    def get_index(self, element:str):
        for index in range(self.set.size):
            if self.set.get(index) == element:
                return index


