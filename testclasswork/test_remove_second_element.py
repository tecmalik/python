from unittest import TestCase
import removesecondelement

class RemoveSecondElement(TestCase):
	def test_if_remove_second_element_exist(self):
		number=[2,3,4,5,6,7,]
		removesecondelement.remove_second_element(number)

	def test_if_remove_second_element_returns_a_list(self):
		number=[2,3,4,5,6,7,]
		value = removesecondelement.remove_second_element(number)
		expected = [2,4,5,6,7]
		self.assertEqual(value, expected)
	def test_if_remove_second_element_returns_0_for_a_single_list(self):
		number=[2]
		value = removesecondelement.remove_second_element(number)
		expected = 0
		self.assertEqual(value, expected)


class PopRemoveFunction(TestCase):
	def test_if_pop_remove_function_exist(self):
		number=[2,3,4,5,6,7,]
		removesecondelement.pop_second_element(number)