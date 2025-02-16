import unittest
from bankapp.bank.bank import bank

class MyBankTest(unittest.TestCase):
    def setUp(self):
        self.my_bank = bank.Bank()
    def test_bank_account_is_empty(self):
        self.assertTrue(self.my_bank.is_empty)
    def test_bank_can_create_an_account(self):
        self.assertTrue(self.my_bank.is_empty)
        self.my_bank.create_account("first_name","last_name","1234")
        self.assertEqual(1 , self.my_bank.get_number_of_accounts)
    def test_bank_can_contain_more_than_one_account(self):
        self.assertTrue(self.my_bank.is_empty)
        self.my_bank.create_account("first_name","last_name","1234")
        self.assertEqual(1 , self.my_bank.get_number_of_accounts)
        self.my_bank.create_account("first_name2","last_name2","1234")
        self.assertEqual(2 , self.my_bank.get_number_of_accounts)
    def test_that_account_created_can_has_account_number(self):
        self.my_bank.create_account("first_name","last_name","1234")
        self.assertEqual(1, self.my_bank.get_account_number("first_name","last_name"))
    def test_that_bank_account_rise_exception_for_invalid_account_details(self):
        self.my_bank.create_account("first_name","last_name","1234")
        with self.assertRaises(Exception): self.my_bank.get_account_number("invalid_first_name","last_name")
        with self.assertRaises(Exception): self.my_bank.get_account_number("first_name","invalid_last_name")
    def test_that_bank_can_check_balance(self):
        self.my_bank.create_account("first_name","last_name","1234")
        self.assertEqual(0,self.my_bank.check_account_balance(1,"1234"))
    def test_that_bank_account_can_be_credited(self):
        self.my_bank.create_account("first_name","last_name","1234")
        self.assertEqual(0,self.my_bank.check_account_balance(1,"1234"))
        self.my_bank.credit_account(1, 10000)
        self.assertEqual(10000,self.my_bank.check_account_balance(1,"1234"))

    def test_that_bank_account_will_raise_error_for_invalid_account_input(self):
        self.my_bank.create_account("first_name","last_name","1234")
        self.assertEqual(0,self.my_bank.check_account_balance(1,"1234"))
        self.my_bank.credit_account(1, 10000)
        self.assertEqual(10000,self.my_bank.check_account_balance(1,"1234"))
        with self.assertRaises(Exception):self.my_bank.check_account_balance(1,"12345")

    def test_that_bank_can_transfer(self):
        self.my_bank.create_account("first_name","last_name","1234")
        self.my_bank.create_account("first_name2","last_name2","1111")
        self.assertEqual(0 , self.my_bank.check_account_balance(1,"1234"))
        self.assertEqual(0 , self.my_bank.check_account_balance(2,"1111"))
        self.my_bank.credit_account(1, 10000)
        self.assertEqual(10000,self.my_bank.check_account_balance(1,"1234"))
        self.my_bank.transfer(1, 5000 , 2 ,"1234")
        self.assertEqual(5000,self.my_bank.check_account_balance(1,"1234"))
        self.assertEqual(5000,self.my_bank.check_account_balance(2,"1111"))
    def test_that_bank_can_find_account_by_account_number(self):
        self.my_bank.create_account("first_name","last_name","1234")
        self.my_bank.create_account("first_name2","last_name2","1111")
        self.assertEqual("first_name2",self.my_bank.find_by_id(2).first_name)
    def test_that_bank_can_delete_account(self):
        self.my_bank.create_account("first_name","last_name","1234")
        self.my_bank.create_account("first_name2","last_name2","1111")
        self.my_bank.delete_account(1,"1234")
        with self.assertRaises(Exception):self.my_bank.find_by_id(1)