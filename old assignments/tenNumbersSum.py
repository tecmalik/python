total = 0
numberCounter=1
while numberCounter < 11:
	firstNumber = int(input("enter numbers "+ str(numberCounter)+" :"))
total = total + firstNumber
numberCounter+=1
print("the total is ",total)