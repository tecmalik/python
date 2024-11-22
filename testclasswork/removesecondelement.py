def remove_second_element(number:list):
	if len(number) > 1:
		number=[2,3,4,5,6,7,]
		number.remove(number[1])
		return number
	else:
		return 0

def pop_second_element(number:list):
	number=[2,3,4,5,6,7,]
	number.pop(1)
	return number

