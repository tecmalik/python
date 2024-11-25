def is_prime_(number):
	counter = 0
	for count in range(1, number):
		if number%count ==0 :
			counter+=1
		elif counter >= 2:
			return False
	return True 