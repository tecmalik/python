def get_switched_list(numbers:list,element):
	switch1 = numbers[:element:] 
	switch2 = numbers[element::] 
	return switch2+switch1