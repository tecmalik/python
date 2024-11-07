sum = 0
number=int(input("Enter a number : "))
for count in range(number): 
	pie =((-1)**count) * 4 / (2*count + 1)
	sum += pie  
print("the value for pie is ", sum)