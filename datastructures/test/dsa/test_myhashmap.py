import unittest

from datastructures.dsa.myhashmap import MyHashMap


class MyHashMapTest(unittest.TestCase):
    def setUp(self):
        self.my_hash_map = MyHashMap()
    def test_that_my_hashmap_is_empty(self):
        self.assertTrue(self.my_hash_map.is_empty())

    def test_my_hash_map_can_add_values_and_key_pairs(self):
        self.my_hash_map.put("key","value")
        self.assertFalse(False)

    def test_my_hash_map_has_a_size_(self):
        self.assertEqual(0,self.my_hash_map.getsize)
        self.my_hash_map.put("key","value")
        self.assertEqual(1,self.my_hash_map.getsize)

    def test_my_hash_map_can_add_more_than_one_keys_and_values(self):
        self.my_hash_map.put("key","value")
        self.my_hash_map.put("key2","value2")
        self.assertEqual(2,self.my_hash_map.getsize)
    def test_my_hash_map_can_dose_not_accept_duplicate_key_(self):
        self.my_hash_map.put("key","value")
        self.my_hash_map.put("key2","value2")
        self.my_hash_map.put("key", "value3")
        self.assertEqual(2,self.my_hash_map.getsize)
        self.assertEqual("value3",self.my_hash_map.get("key"))