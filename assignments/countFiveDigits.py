
negativeCounter = 0
positiveCounter = 0
zeroCounter = 0
numberCounter = 1
print('Enter five numbers')
zeroNumbers = 0
positiveNumbers = 0
negativeNumbers = 0
			
while numberCounter <= 5:
	newNumber = int(input('Enter number :'))
	numberCounter = numberCounter + 1
			
	if (newNumber > 0) :
		positiveNumbers = 1 + positiveCounter

	elif newNumber < 0 :
		negativeNumbers = 1 + negativeCounter
  
	if newNumber == 0 :
		zeroNumbers = 1 + zeroCounter
			
print('The number of positive is' , positiveNumbers )
print('The negative number is' , negativeNumbers)
print('The number of zeros is' , zeroNumbers)
