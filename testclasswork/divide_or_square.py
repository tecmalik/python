import math
def get_divide_or_square(number):
	square = 0
	result = 0
	if number % 5 == 0:
		result = math.sqrt(number)
		square = round(result,2)
		return square
	if number%5 != 0:
		remender = number%5
		return remender
	if number < 0 and number%5 == 0:
		return "valueerror"
	if number not in [float, int] :
		return "typeError" 