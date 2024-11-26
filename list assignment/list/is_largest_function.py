def is_largest(numbers:list):
	largest = numbers[0]
	for number in numbers:
		if number>largest:
			largest = number
	return largest