def even_bool(numbers):
	return numbers% 2 == 0 

print(even_bool(10))


def even_boo2(numbers:list):
	return [True if x % 2 == 0 else False for x in numbers ]

print(even_boo2([10,3,7,1,9,4,2,8,5,6]))

def even_boo3(numbers:list):
	return [ x % 2 == 0 for x in numbers ]

print(even_boo3([10,3,7,1,9,4,2,8,5,6]))

def to_capital(words):
	return[word.title() for word in words]

print(to_capital(['red','orange','yellow','green','blue']))

def multiple_3():
	return[ x for x in range(3, 31 , 3)]

print(multiple_3())

def square_odd(numbers):
	return[x**2 for x in numbers if x % 2 != 0 ]

print(square_odd([10,3,7,1,9,2,8,5,6]))


# filters and maps 

def is_odd(x):
	return x%2!= 0

numbers = [10,3,7,1,9,4,2,8,5,6]
holder = list(filter(is_odd, numbers))
print(holder)
	
#output[3,7,1,9,5]

numbers = [10,3,7,9,4,2,8,5,6]

container = list(filter(lambda x:x%2!=0,numbers))
print(container)
# output = [3, 7, 9, 5]
