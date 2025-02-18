from xml.etree.ElementTree import tostring

from mydiary.diary.diary.entry import Entry

class Diary:
    def __init__(self,username,password):
        self._entries = []
        self._username = username
        self.__password = password
        self._isLocked = False
        self.count = 0

    def __str__(self):
        return self._username

    def is_locked(self):
        return self._isLocked

    def lock(self):
        self._isLocked = True
    def unlock(self,password):
        if password != self.__password:
            raise Exception('password does not match')
        if password == self.__password:
            self._isLocked = False

    def create_entry(self,title:str,body:str):
        if self._isLocked:
            raise Exception('Diary is locked')
        if title == "" or body == "":
            raise Exception('Diary is empty')
        self._entries.append(Entry(self.__id_number(), title, body))

    def number_of_entries(self):
        return len(self._entries)

    def __id_number(self):
        self.count += 1
        return self.count

    def delete(self, number:int):
        if number < 1 or number > self.number_of_entries():
            raise Exception('invalid diary number')
        if self.is_locked():
            raise Exception('Diary is locked')
        for entry in self._entries:
            if entry.get_id_number() == number:
                self._entries.remove(entry)

    def find_by_id(self, id_number:int):
        if id_number < 1 or id_number > self.number_of_entries():
            raise Exception('invalid diary id')
        if self.is_locked():
            raise Exception('Diary is locked')
        for entry in self._entries:
            if entry._idNumber == id_number:
                return entry

    def update_entry(self, id_number:int, updated_title:str, updated_body:str):
        if id_number < 1 or id_number > self.number_of_entries():
            raise Exception('invalid diary id')
        if self.is_locked():
            raise Exception('Diary is locked')
        if updated_title == "" or updated_body == "":
            raise Exception('Diary is empty')
        for entry in self._entries:
            if entry.idNumber == id_number:
                entry.set_title(updated_title)
                entry.set_body(updated_body)
    @property
    def get_username(self):
        return self._username

    def verify_password(self,password):
        if password == "":
            raise Exception('password is empty')
        if password != self.__password:
            raise Exception('password does not match')
        return password == password



