def get_sum(number:list):
	total=0
	counter=0
	for count in number:
		total+=count
		counter+=1
	
	sum=(total*counter)-total
		
	return sum
		