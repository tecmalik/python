numberCounter = 0
product = 0
count = -1;
number = int (input("Enter a number : "))
while numberCounter <= number:
	product = number * numberCounter 
	count = count + 1
	print(f"{number} x { numberCounter } = {product}")
	numberCounter += 1

