def element_with_even_position(number:list):
	index=[]
	for count in range (1,len(number),2):
		if count%2== 0:
			index.append(number[count])
	return index
