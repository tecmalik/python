def get_factoria(number):
	factoria = 0
	for count in range(1, number):
		factoria*=number
		number-1
	return factoria