#write a function that takes a string and returns the number of vowels in the string. 
# example: input "python is sweet"
# output:4
def checkingvowels(userinput):
	number = 0	
	for count in (userinput):
		if count == ['A' , 'E' , 'I' , 'O' , 'U', 'a', 'e', 'i' , 'o' , 'u']:
			number = int (number + 1)
			
	return"number"	

userinput = input("Enter a sentence :")

print(checkingvowels(userinput))