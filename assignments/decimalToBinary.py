number = int(input('enter a number:'))

binary = ""


while number != 0 :
	rem = number % 2
	number //= 2
	binary = str(rem) + binary
	
	
print(binary) 