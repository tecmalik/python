def get_prime_numbers(number):
	allprimenumbers=[]
	for prime in range (2, number):
		count = 0
		for divisor in range (1 , prime):
			if prime%divisor == 0:
				count += 1
		if count == 1 :
			allprimenumbers.append(prime)
	return allprimenumbers
					 