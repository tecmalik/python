number = int(input('Enter a five-digit number:')) 

while number > 0 :
	digit = number % 10
	print(digit ,end=" ")
	number = number // 10

