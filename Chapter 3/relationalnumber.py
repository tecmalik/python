print('Enter two integers and i will tell you the relationships they satisfy')

numberone = int(input('Enter first number: ')) 
numbertwo = int(input('Enter second number: ')) 

if (numberone > numbertwo):
	print(numberone, 'is greater', numbertwo)
	if (numberone >= numbertwo):
		print(numberone , 'is greater than or equal to', numbertwo)
	if (numberone != numbertwo ):
		print(numberone , 'is not equal to', numbertwo)


elif (numberone < numbertwo ):
	print(numberone, 'is less', numbertwo)
	if (numberone <= numbertwo):
		print(numberone , 'is less than or equal to', numbertwo)
	if  (numberone != numbertwo): 
		print(numberone , 'is not equal to', numbertwo)
else:
	print(numberone , 'is equal to', numbertwo)




