

def isEven(number):
	if number %2 == 0:
		return True
	return False
def isPrime(number):
	counter=0
	for count in range (1,number):
		if number%count == 0:
			counter+=1
		if counter >= 2:
			return False
	return True
def subtract(integer , integer2):
	if integer2 > integer:
		return integer2 -integer
	else:
		return integer - integer2
def divide(integer , integer2)->float:
	return integer/integer2
def factorOfNumber(integer):
	factors =[]
	for count in range (1 , integer+1):
		if integer%count == 0:
			factors.append(count)
	return factors
def isSquare(integer):
	for count in range (integer//2):
		if count*count == integer:
			return True
	return False
def isPallindrum(integer):
	counter=0
	while integer >0 :
		if integer[counter] != integer[4-counter]:
			return false
	counter+=1
	
def factoriaOf(integer):
	factor = []
	for count in range (1,integer+1):
		if integer%count == 0:
			factor.append(count)
	return factor
def squareOf(integer):
	return integer*integer
 