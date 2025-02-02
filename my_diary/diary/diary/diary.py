from my_diary.diary.diary.entry import Entry
from phaseGateOne.firstTask.task4 import count





class Diary:
    def __init__(self,username,password):
        self.entries = []
        self.username = username
        self.password = password
        self.isLocked = False
        self.count = 0

    def is_locked(self):
        return self.isLocked

    def lock(self):
        self.isLocked = True
    def unlock(self,password):
        if password == self.password:
            self.isLocked = False

    def create_entry(self,title:str,body:str):
        if self.isLocked:
            raise Exception('Diary is locked')
        if title == "" or body == "":
            raise Exception('Diary is empty')
        self.entries.append(Entry(self.id_number(), title, body))

    def number_of_entries(self):
        return len(self.entries)

    def id_number(self):
        self.count += 1
        return self.count

