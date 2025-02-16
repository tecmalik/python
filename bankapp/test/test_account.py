
import unittest
from bankapp.bank.bank import account

class MyAccountTest(unittest.TestCase):
    def setUp(self):
        self.my_account = account.Account("firstname","lastname","1234", 1)
    def test_that_account_is_empty(self):
        self.assertTrue(self.my_account.is_empty)
    def test_that_i_can_check_my_account_balance(self):
        self.assertEqual(0, self.my_account.check_balance("1234"))
    def test_that_account_will_raise_exception_to_check_my_account_balance_with_invalid_pin(self):
        with self.assertRaises(Exception): self.my_account.check_balance("12345")
        with self.assertRaises(Exception): self.my_account.check_balance("errt")
        with self.assertRaises(Exception): self.my_account.check_balance("3453")
    def test_that_i_can_credit_my_account_(self):
        self.assertEqual(0, self.my_account.check_balance("1234"))
        self.assertFalse(self.my_account.credit(100))
        self.assertEqual(100, self.my_account.check_balance("1234"))
    def test_that_i_can_not_accept_negative_deposit_to_my_account_(self):
        self.assertEqual(0, self.my_account.check_balance("1234"))
        with self.assertRaises(Exception):(self.my_account.credit(-100))
    def test_my_account_can_update_my_pin_(self):
        self.assertEqual(0, self.my_account.check_balance("1234"))
        self.my_account.update_pin("1234","1111")
        with self.assertRaises(Exception):(0, self.my_account.check_balance("1234"))
        self.assertEqual(0, self.my_account.check_balance("1111"))
    def test_my_account_can_raise_error_to_update_with_invalid_pin_(self):
        self.assertEqual(0, self.my_account.check_balance("1234"))
        with self.assertRaises(Exception):self.my_account.update_pin("12p4","1111")
        self.assertEqual(0, self.my_account.check_balance("1234"))
    def test_that_my_account_can_be_debited(self):
        self.assertEqual(0, self.my_account.check_balance("1234"))
        self.assertFalse(self.my_account.credit(100))
        self.assertEqual(100, self.my_account.check_balance("1234"))
        self.my_account.debit(50)
        self.assertEqual(50, self.my_account.check_balance("1234"))
    def test_that_my_account_can_no_allow_debit_above_balance(self):
        self.assertEqual(0, self.my_account.check_balance("1234"))
        self.assertFalse(self.my_account.credit(100))
        self.assertEqual(100, self.my_account.check_balance("1234"))
        with self.assertRaises(Exception): self.my_account.debit(500)
        self.assertEqual(100, self.my_account.check_balance("1234"))







