import unittest
from encrypt_text import encrypt_text

class EncryptTextROT13(unittest.TestCase):
    def test_if_encrypt_function_exist(self):
        encrypt_text.get_encrypt_text("text")
    def test_if_decrypt_function_will_return_a_string(self):
        encrypt_text.get_encrypt_text("Hello,World!")
        self.assertEqual("Uryyb,jbeyq!", encrypt_text.get_encrypt_text("Hello,World!"))
    def test_if_encrypt_function_returns_a_correct_string_value(self):
        encrypt_text.get_encrypt_text("welcome123")
        self.assertEqual("jrypbzr,123", encrypt_text.get_encrypt_text("welcome,123"))

