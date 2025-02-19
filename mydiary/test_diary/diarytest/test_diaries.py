import unittest

from mydiary.diary.diary import diaries
from mydiary.diary.diary import diary

class MyDiariesTestCase(unittest.TestCase):
    def setUp(self):
        self.my_diaries = diaries.Diaries()
    def test_that_my_diaries_can_contain_my_diary(self):
        self.my_diaries.add("username","password")
        self.assertEqual(1, self.my_diaries.get_size())
    def test_that_my_diaries_can_contain_more_than_a_diary(self):
        self.my_diaries.add("username","password")
        self.my_diaries.add("username2","password2")
        self.assertEqual(2, self.my_diaries.get_size())
    def test_that_i_can_find_my_diary_by_username_t_in_diaries(self):
        self.my_diaries.add("username","password")
        self.my_diaries.add("username2","password2")
        self.assertEqual( diary.Diary("username2","password2").get_username , self.my_diaries.find_by_username("username2").get_username )

    def test_that_my_diaries_can_delete_my_diary(self):
        self.my_diaries.add("username","password")
        self.my_diaries.add("username2","password2")
        self.my_diaries.delete("username","password")
        self.assertEqual(1, self.my_diaries.get_size())
