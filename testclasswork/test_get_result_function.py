from unittest import TestCase
import get_result_function

class GetResultFunction(TestCase):
	def test_if_get_result_exist(self):
		get_result_function.get_result(23,23,23)
	