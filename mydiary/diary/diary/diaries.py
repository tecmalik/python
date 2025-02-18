
from mydiary.diary.diary.diary import Diary

class Diaries:
    def __init__(self):
        self.diaries = []

    def add(self, username:str , password:str):
        self.diaries.append(Diary(username, password))

    def get_size(self):
        return len(self.diaries)

    def find_by_username(self, username:str):
        matched_acct = 0
        for diary in self.diaries:
            if diary.__str__() == username:
                matched_acct += 1
                return diary
        if matched_acct == 0 : raise Exception("Diary not found")

    def delete(self, username:str , password:str):
        if not self.find_by_username(username).verify_password(password):
            raise Exception("Diary not found")
        self.diaries.remove(self.find_by_username(username))
