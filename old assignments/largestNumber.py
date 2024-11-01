
numberCounter = 0
largestNumber = 0
smallestNumber = 0
		
firstNumber = int(input("Enter a number or exit with -1:"))
if firstNumber == -1:
	print(" no number was inputed")
else:					
	largestNumber = firstNumber;
	smallestNumber = firstNumber;
	while firstNumber != -1:
		if firstnumber ==-1:
			brake
		firstNumber =int(input("Enter a number or exit with -1:"))
		if firstNumber > largestNumber :
			largestNumber = firstNumber
		if firstNumber < smallestNumber:			smallestNumber = firstNumber
		numberCounter+= 1
	print(largestNumber," is the largest number")
	print(smallestNumber," is the smallest number")