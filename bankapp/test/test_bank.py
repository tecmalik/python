import unittest
from bankapp.bank.bank import bank

class MyBankTest(unittest.TestCase):
    def setUp(self):
        self.my_bank = bank.Bank()
    def test_bank_account_is_empty(self):
        self.assertTrue(self.my_bank.is_empty)  # add assertion here



