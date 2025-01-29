from data_structures.dsa.myarraylist import MyArrayList


class MySet:
    def __init__(self):
        self.set = MyArrayList()
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def add(self, value:str):
        self.set.add(value)
        self.size += 1


