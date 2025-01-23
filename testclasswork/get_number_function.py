def get_number(number , numbers:list):
	index = 0
	for count in range (len(numbers)):
		if numbers[count] == number :
			index = count
			return index
	return "not present"

def get_positive_nagative_numbers(numbers:list):
	positivecount = 0
	negativecount = 0
	zeros = 0
	for number in numbers:
		if number > 0:
			positivecount += 1
		elif number < 0:
			negativecount+= 1
		elif number == 0:
			zeros += 1
	return positivecount, negativecount, zeros 
		
		
	