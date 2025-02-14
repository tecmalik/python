


class Account:
    def __init__(self, username, pin):
        self.username = username
        self.pin = pin
        self.balance = 0

    # def validate(password:str):
      # return self.pin == password and (password) == 4 and password.isdigit()

        # @property
        # def is_empty(self, password:str):
        # if validate(password) == False:
        #     return Exception('invalid details')
        # return self.balance == 0

    def deposit(self, amount:int):
        if amount <= 0:
             raise Exception('amount must be positive')
        self.balance += amount

    def withdraw(self, amount:int):
        if amount > self.balance:
            raise Exception('Not enough money!')
        if amount <= 0:
            raise Exception('amount must be positive')
        if type(amount) is not int :
            raise Exception('amount must be of type int')
        self.balance -= amount