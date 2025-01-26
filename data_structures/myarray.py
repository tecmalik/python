
class MyArray:
    def __init__(self ,size):
        self.array = []
        self.length = size
        self.size = 0

    def isempty(self):
        return self.size == 0

    def myappend(self, item):
        if (self.size < self.length):
            self.array += item
            self.size += 1
        return "index out of bound"

    def mylength(self):
        return self.length

    def get(self , index:int):
        if (index < self.length):
            return self.array[index]
        return F"index out of bound for length {index}"
    def __str__(self):
        return str(self.array)








