
import unittest
from bankapp.bank.bank import account

class MyAccountTest(unittest.TestCase):
    def setUp(self):
        self.my_account = account.Account("username", "pin")
    def test_that_account_is_empty(self):
        self.assertTrue(self.my_account.is_empty)
    def test_that_i_can_check_my_account_balance(self):
        self.assertEqual(0, self.my_account.balance("pin"))
    def test_that_i_can_deposit_to_my_account_(self):
        self.assertEqual(0, self.my_account.balance("pin"))
        self.assertFalse(self.my_account.deposit(100))
        self.assertEqual(100, self.my_account.balance("pin"))
    def test_my_account_can_update_my_pin_(self):
        pass


