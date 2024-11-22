def get_even_sum(number)->int:
	total = 0
	for count in number:
		if count % 2 == 0:
			total+=count
	return total
	