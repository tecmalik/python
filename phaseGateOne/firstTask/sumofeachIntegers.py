integer = int(input("Enter integer between 0 and 100 : "))
sum = 0
eachdigit = 0
while integer>0:
	eachdigit = integer%10 
	sum += eachdigit
	integer=integer//10
print(f"the sum is {sum}")