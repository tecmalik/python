from datetime import datetime, date


class Entry:
    def __init__(self,id_number,title,body):
        self._idNumber = id_number
        self._title = title
        self._body = body
        self._date = date.today()

    @property
    def idNumber(self):
        return self._idNumber

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
        return self._date

    @date.setter
    def date(self,date):
        self._date = date.today()
    @property
    def idNumber(self):
        return self._idNumber

    def __str__(self):
        return (f" {self.title} : {self._date} \n {self.body}")






