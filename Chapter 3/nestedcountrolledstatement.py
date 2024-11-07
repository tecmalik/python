firstlargest = 0
secondlargest = 0
for count in range (1 , 11):
	number= int(input("Enter number : "))
	if number > firstlargest:
		firstlargest = number 
	if number > secondlargest and number != firstlargest :
		secondlargest = number
print("first largest number is ", firstlargest)
print("second largest number is ", secondlargest)