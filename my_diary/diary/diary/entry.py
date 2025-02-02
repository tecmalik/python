from datetime import datetime

class Entry:
    def __init__(self,idNumber,title,body):
        self.idNumber = idNumber
        self.title = title
        self.body = body
        self.date = datetime.now()

    def getIdNumber(self):
        return self.idNumber
    def getTitle(self):
        return self.title
    def getBody(self):
        return self.body
    def getDate(self):
        return self.date


