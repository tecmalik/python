from unittest import TestCase
import onlyfloatsfunction
	
class OnlyfloatsFunction(TestCase):
	def test_if_only_floats_exist(self):
		onlyfloatsfunction.getonly_floats(2.3,2.4)

	def test_if_a_float_and_a_floats_will_retur_result(self):
		actual = onlyfloatsfunction.getonly_floats(2.2,2.4)
		expected = 1
		self.assertEqual(actual,expected)
		
	
	def test_if_an_int_and_a_floats_will_retur_0_result(self):
		actual = onlyfloatsfunction.getonly_floats(2,2.4)
		expected = 0
		self.assertEqual(actual,expected)
	
	def test_if_an_nagative_int_and_a_floats_will_retur_0_result(self):
		actual = onlyfloatsfunction.getonly_floats(-2,2.4)
		expected = 0
		self.assertEqual(actual,expected)

	def test_if_an_nagative_float_and_a_nagative_floats_will_retur_1_result(self):
		actual = onlyfloatsfunction.getonly_floats(-2.4,-2.4)
		expected = 1
		self.assertEqual(actual,expected)

	def test_if_an_int_and_an_int_will_retur_result(self):
		actual = onlyfloatsfunction.getonly_floats(2,2)
		expected = 0
		self.assertEqual(actual,expected)
	def test_if_a_nagative_int_and_a_nagative_int_will_retur_result(self):
		actual = onlyfloatsfunction.getonly_floats(-2,-2)
		expected = 0
		self.assertEqual(actual,expected)