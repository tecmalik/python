	
numberCounter = 0
secondNumber = 0
firstNumber = 0
thirdNumber = 0

while (numberCounter < 3):
	++numberCounter;
	
	firstNumber = int(input(" Enter a number : "))
	secondNumber = int(input(" Enter a number : "))
	thirdNumber = int(input(" Enter a number : "))
		
	if firstNumber < secondNumber and secondNumber < thirdNumber :
		print(" Numbers are in increasing order ")
		
	elif firstNumber > secondNumber and secondNumber> thirdNumber:
		print(" Numbers are in decreasing order ")
	else :
		print(" Numbers are not in order ")
		