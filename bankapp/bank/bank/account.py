def is_pin(entered_pin):
    if not entered_pin.isdigit():
        return False
    if len(entered_pin) > 4:
        return False
    return True


class Account:
    def __init__(self, first_name,last_name,pin, account_number ):
        self._first_name = first_name
        self._last_name = last_name
        self._pin = pin
        self._account_number = account_number
        self._balance = 0


    @property
    def is_empty(self):
        return self._balance == 0

    def is_valid(self,entered_pin):
        if not entered_pin.isdigit():
            raise Exception("Invalid PIN details")
        if len(entered_pin) > 4:
            raise Exception("Invalid PIN details")
        return self._pin == entered_pin

    def check_balance(self,pin:str):
        if not self.is_valid(pin) :
            raise Exception('Invalid PIN')
        return self._balance

    @property
    def first_name(self):
        return self._first_name
    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name
    @property
    def last_name(self):
        return self._last_name
    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name
    @property
    def account_number(self):
        return self._account_number
    @account_number.setter
    def account_number(self, account_number):
        self._account_number = account_number


    def deposit(self, amount:int):
        if amount <= 0:
             raise Exception('amount must be positive')
        self._balance += amount

    def debit(self, amount:int):
        if amount > self._balance:
            raise Exception('Not enough money!')
        if amount <= 0:
            raise Exception('amount must be positive')
        if type(amount) is not int :
            raise Exception('amount must be of type int')
        self._balance -= amount

    def update_pin(self, old_pin, new_pin):
        if not self.is_valid(old_pin):
            raise Exception("Invalid PIN details")
        if not is_pin(old_pin):
            raise Exception("Invalid PIN details")
        self._pin = new_pin


