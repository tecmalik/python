from datastructures.dsa.myarray import MyArray
from datastructures.dsa.myarraylist import MyArrayList
from datastructures.dsa.myset import MySet


class MyHashMap:
    def __init__(self):
        self.size = 0
        self.keys = MySet()
        self.value = MyArrayList()


    def put(self, key, value):
        if self.keys.my_contains(key):
            key_index = self.keys.get_index(key)
            self.value.insert(key_index, value)
        else :
            self.keys.add(key)
            self.value.add(value)
            self.size = self.size + 1

    def is_empty(self):
        return self.size == 0

    @property
    def getsize(self):
        return self.size

    def get(self, element):
        if self.keys.my_contains(element):
            index_element = self.keys.get_index(element)
            return self.value.get(index_element)

    def contains(self, element):
        if self.keys.my_contains(element):
            return True

