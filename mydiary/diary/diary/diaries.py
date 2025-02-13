from my_diary.diary.diary import diary
from my_diary.diary.diary.diary import Diary


class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username:str , password:str):
        self.diaries.append(Diary(username, password))

    def get_size(self):
        return len(self.diaries)

    def find_by_username(self, username:str):
        for diary in self.diaries:
            if diary.get_username == username:
                return diary
        raise Exception("Diary not found")

    def delete(self, username:str):
        self.diaries.remove(self.find_by_username(username))