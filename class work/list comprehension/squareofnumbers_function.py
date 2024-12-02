def squareofnumbers(number):
	return[number*number for number in range(1,number+1)]

def numbersgreaterthan10(numbers:list):
	return[tenth for tenth in numbers if tenth>10 ]

def ispallindromboolean(words):
	return [word == word[::-1] for word in words] 

def getnumbers(rubbish:list):
	return [int(value) for value in rubbish if value.isdigit()]

def getnumbers2(rubbish:list):
	return [int(value) for value in rubbish if value.isnumeric()]


def getnumbersofcharacters(words:list , number):
	return [word for word in words if len(word) == number]

def getsumnumbers(number):
	return sum([ int (x) for x in str(number)])

def nonvowel(words:list):
	return [character for character in words if character not in['a','e','i','o','u','A','E','I','O','U'] ]
	
return sum(list map(lamda num:int(num),str(number)))




print(squareofnumbers(4))
print(numbersgreaterthan10([1,5,12,15,8]))
print(ispallindromboolean(["madam","boy","mmamm"]))
print(getnumbers('abd123def456'))
print(getnumbers2('abd123def456'))
print(getnumbersofcharacters(['orrange', 'apple' , 'ice' , 'beans' , 'rice'],5))
print(getsumnumbers(123924))
print(nonvowel(['orrange', 'apple' , 'ice' , 'beans' , 'rice']))














#return list(map(lambda word:word == word[::-1], words))

#def ispalindrom(word):
#	count=0
#	for character in word:
#		count+=1
#	check = count//2
#	for i in range (1,check):
#		if word[i] != word[count-i]:
#			return False
#	return True

