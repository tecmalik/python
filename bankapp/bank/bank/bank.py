from bankapp.bank.bank.account import Account

class Bank:
    def __init__(self,):
        self.accounts = []
        self._id_number = 0
        self.size = 0

    is_empty = True

    def create_account(self, first_name, last_name, pin):
        self._id_number += 1
        account = Account(first_name, last_name, pin, self._id_number)
        self.accounts.append(account)
        self.size +=1
    @property
    def get_number_of_accounts(self):
        return self.size

    def get_account_number(self, first_name,last_name):
        account_match = 0
        for account in self.accounts:
            if account.first_name == first_name and account.last_name == last_name:
                account_match += 1
                return account.account_number
        if account_match == 0:
            raise Exception('Account number not found')

    def check_account_balance(self, account_number, pin):
        for account in self.accounts:
            if account.account_number == account_number:
                return account.check_balance(pin)

    def credit_account(self, account_number, amount):
        for account in self.accounts:
            if account.account_number == account_number:
                account.credit(amount)

    def transfer(self, senders_account_number:int, amount_to_transfer:int, recipient_account_number:int, pin:str):
        if not self.validate_accounts(senders_account_number, recipient_account_number):
            raise Exception('Invalid account number')
        for account in self.accounts:
            if account.account_number == senders_account_number and account.check_balance(pin) >= amount_to_transfer:
                account.debit(amount_to_transfer)
            if account.account_number == recipient_account_number:
                account.credit(amount_to_transfer)


    def validate_accounts(self,senders_account,recipient_account):
        matched_account = 0
        for account in self.accounts :
            if account.account_number == senders_account:
                matched_account += 1
            if account.account_number == recipient_account:
                matched_account += 1
        return matched_account == 2




