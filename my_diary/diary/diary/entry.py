from datetime import datetime

class Entry:
    def __init__(self,idNumber,title,body):
        self.idNumber = idNumber
        self.title = title
        self.body = body
        self.date = datetime.now()

    def get_id_number(self):
        return self.idNumber
    def get_title(self):
        return self.title
    def get_body(self):
        return self.body
    def get_date(self):
        return self.date
    def set_title(self,title):
        self.title = title
    def set_body(self,body):
        self.body = body



