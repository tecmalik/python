import time 
from random import randrange 

passcount = 0
failcount = 0
answer = 0
for count in range (1,11):
	firstNumber = randrange(1,100)
	secondNumber = randrange(1,100)
	if firstNumber > secondNumber:
		answer = input(f"Subtract {firstNumber} from {secondNumber} what will the answer be ?" )
		if answer == firstNumber-secondNumber:
			passcount +=1
		else: 
			 failcount+=1
	else :
		answer = input(f"Subtract {secondNumber} from  {firstNumber}what will teh anser be ?" )
		if answer == secondNumber-firstNumber:
			passcount +=1
		else: 
			 failcount+=1

print(f" you Score {passcount} of 10 and failed {failcount} ")