def is_even_list(numbers:list):
	result = []
	for number in numbers:
		if number%2 == 0:
			result.append(True)
		if number%2 != 0:
			result. append(False)
	return result