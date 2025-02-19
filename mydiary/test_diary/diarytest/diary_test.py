import unittest

from mydiary.diary.diary import diary


class Diary(unittest.TestCase):
    def setUp(self):
        self.my_diary = diary.Diary("username", "password" )
    def test_that_my_diary_is_not_locked(self):
         self.assertEqual( False , self.my_diary.is_locked())
    def test_that_my_diary_can_be_locked(self):
        self.my_diary.lock()
        self.assertEqual( True , self.my_diary.is_locked())
    def test_that_my_diary_can_be_unlocked(self):
        self.my_diary.lock()
        self.assertEqual( True , self.my_diary.is_locked())
        self.my_diary.unlock("password")
        self.assertEqual( False, self.my_diary.is_locked())
    def test_that_my_diary_throw_an_error_fo_incorrect_details(self):
        self.my_diary.create_entry("Title","body")
        self.my_diary.lock()
        with self.assertRaises(Exception) :self.my_diary.unlock("incorrect_password")
    def test_that_i_can_Create_an_entry_in_diary(self):
        self.my_diary.create_entry("Title","Body")
        self.assertEqual(1 ,self.my_diary.number_of_entries())
        with self.assertRaises( Exception ): self.my_diary.create_entry("","")
    def test_that_my_diary_can_create_multiple_entry(self):
        self.my_diary.create_entry("Title","Body")
        self.my_diary.create_entry("Title1","Body1")
        self.my_diary.create_entry("Title2","Body2")
        self.assertEqual(3,self.my_diary.number_of_entries())
    def test_that_my_diary_can_delete_Entry(self):
        self.my_diary.create_entry("Title","Body")
        self.my_diary.create_entry("Title1","Body1")
        self.my_diary.create_entry("Title2","Body2")
        self.assertEqual(3,self.my_diary.number_of_entries())
        self.my_diary.delete(2)
        self.assertEqual(2,self.my_diary.number_of_entries())
    def test_that_my_diary_will_raise_error_for_invalid_id(self):
        self.my_diary.create_entry("Title","Body")
        with self.assertRaises( Exception): self.my_diary.delete(2)
    def test_that_my_diary_will_raise_error_if_diary_is_locked(self):
        self.my_diary.create_entry("Title","Body")
        self.my_diary.lock()
        self.assertEqual( True, self.my_diary.is_locked())
        with self.assertRaises( Exception ): self.my_diary.delete(1)
    def test_that_my_diary_can_find_by_id_entry_by_id(self):
        self.my_diary.create_entry("Title","Body")
        self.my_diary.create_entry("Title1","Body1")
        self.my_diary.create_entry("Title2","Body2")
        self.assertEqual("Title1",self.my_diary.find_by_id(2).title)
    def test_that_my_diary_can_raise_error_to_find_invalid_id_entry(self):
        self.my_diary.create_entry("Title","Body")
        with self.assertRaises( Exception): self.my_diary.find_by_id(7)
    def test_that_find_by_id_will_raise_error_when_diary_is_locked(self):
        self.my_diary.create_entry("Title","Body")
        self.my_diary.lock()
        self.assertEqual( True, self.my_diary.is_locked())
        with self.assertRaises(Exception): self.my_diary.find_by_id(1)
    def test_That_my_diary_can_update_entry(self):
        self.my_diary.create_entry("Title","Body")
        self.my_diary.create_entry("Title1","Body1")
        self.my_diary.update_entry(1,"updatedTitle","updatedBody2")
        self.assertEqual("updatedTitle",self.my_diary.find_by_id(1).title)
    def test_That_my_diary_will_raise_error_for_Invalid_update(self):
        self.my_diary.create_entry("Title","Body")
        self.my_diary.create_entry("Title1","Body1")
        with self.assertRaises(Exception): self.my_diary.update_entry(6,"updatedTitle","updatedBody2")
    def test_that_my_diary_can_raise_error_for_update_when_my_diary_is_locked(self):
        self.my_diary.create_entry("Title","Body")
        self.my_diary.lock()
        self.assertEqual( True, self.my_diary.is_locked())
        with self.assertRaises(Exception): self.my_diary.update_entry(1,"updatedTitle","updatedBody2")
    def test_that_my_diary_raises_an_error_for_no_input(self):
        self.my_diary.create_entry("Title","Body")
        with self.assertRaises( Exception): self.my_diary.update_entry(1,"","")
    

