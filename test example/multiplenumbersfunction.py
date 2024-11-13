def get_multiple(first_number,second_number):
	if type(first_number) in [int, float] and type(second_number) in [int]:
		multiple = 0
		
		for count in range(second_number):
			multiple += first_number 
	
		return multiple