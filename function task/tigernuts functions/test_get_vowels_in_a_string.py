from unittest import TestCase
import getvowelsinastring

class GetVowels(TestCase):
	def test_if_get_vowels_in_a_string_function_exist(self):
		 getvowelsinastring.get_vowels_in_a_string("python is sweet")
	
	def test_if_get_vowels_in_a_string_function_returns_a_value(self):
		value =getvowelsinastring.get_vowels_in_a_string("python is sweet")
		expected = 4
		self.assertEqual(value,expected)
	
	def test_if_get_vowels_in_a_string_function_returns_a_value_if_smallerlatters_are_inputed(self):
		value =getvowelsinastring.get_vowels_in_a_string("python is sweet")
		expected = 4
		self.assertEqual(value,expected)
	
	def test_if_get_vowels_in_a_string_function_returns_a_value_if_capital_latters_are_inputed(self):
		value =getvowelsinastring.get_vowels_in_a_string("python is sweet")
		expected = 4
		self.assertEqual(value,expected)
	def test_if_get_vowels_in_a_string_function_returns_a_value_if_a_number_inputed(self):
		self.assertRaises(TypeError, getvowelsinastring.get_vowels_in_a_string, 23)
		
# classwork	
	
import get_sumofnumber
class Get_Sumofnumber(TestCase):
	def test_if_test_of_number_returns_a_value(self):
		value = get_sumofnumber.get_sum([1,2,3,4,5])
		expected = 60
		self.assertEqual(value,expected)


import sorted
class SortedFunction(TestCase):
	def test_if_get_sorted_function_exist(self):
		firstnumber = [3,4,9,10]
		secondnumber = [1,5,7,8,0,-1]
		value = sorted.sorted_function(firstnumber,secondnumber)
		expected = [-1,0,1,3,4,5,7,8,9,10]
		self.assertEqual(value,expected)
		
#end of classwork


import get_similarities

class GetSimilaritiesFunction(TestCase):
	def test_if_get_get_similarities_function_exist(self):
		get_similarities.get_similarities_function(firstnumber,secondnumber)
	
	
		


		
	
