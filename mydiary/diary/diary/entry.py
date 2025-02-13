from datetime import datetime

class Entry:
    def __init__(self,id_number,title,body):
        self._idNumber = id_number
        self._title = title
        self._body = body
        self._date = datetime.now()

    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        self._title = title

    @property
    def body(self):
        return self._body
    @body.setter
    def body(self,body):
        self._body = body

    @property
    def date(self):
        day_of_week = self._date.weekday()
        day_of_month = self._date.d
        return str(self._date) + " Hello"

    @date.setter
    def date(self,date):
        self._date = date









