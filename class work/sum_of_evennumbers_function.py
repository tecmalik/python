def sum_of_evennumbers(numbers:list):
	total = 0
	for digits in numbers:
		if digits%2 == 0:
			total += digits
	return total