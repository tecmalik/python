def breaking_a_list(numbers:list):
	index1 = 0
	length = 0
	firstlist=[]
	secondlist=[]
	for number in numbers:
		length+=1 
	for count in range(length):
		if count <= length//2:
			firstlist.append(numbers[index1])
			index1+=1
		if count >length//2:
			secondlist.append(numbers[index1])
			index1+=1
	result = [firstlist,secondlist]
	return result