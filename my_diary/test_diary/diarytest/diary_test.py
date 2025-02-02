import unittest

from my_diary.diary.diary import diary


class Diary(unittest.TestCase):
    def setUp(self):
        self.my_diary = diary.Diary("username", "password" )
    def test_that_my_diary_is_not_locked(self):
         self.assertEqual( False , self.my_diary.is_locked())
    def test_that_my_diary_can_be_unlocked(self):
        self.my_diary.lock()
        self.assertEqual( True , self.my_diary.is_locked())
    def test_that_my_diary_can_be_locked(self):
        self.my_diary.lock()
        self.assertEqual( True , self.my_diary.is_locked())
        self.my_diary.unlock("password")
        self.assertEqual( False, self.my_diary.is_locked())
    def test_that_i_can_Create_an_entry_in_diary(self):
        self.my_diary.create_entry("Title","Body")
        self.assertEqual(1 ,self.my_diary.number_of_entries())





