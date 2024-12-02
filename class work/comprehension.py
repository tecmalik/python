def comprehension1():
	return[i for i in range(1,6)] 
def comprehension2():
	return[i for i in 'number']
def comprehension3():
	return(sum([i for i in range(1,6)]))
def comprehension4():
	return(get_total([i for i in range(1,6)]))
def comprehension5():
	return(get_cube([i for i in range(1,6)]))
def comprehension6():
	return([i**3 for i in range(1,6)])



def get_total(numbers:list):
	total=0
	for number in numbers:
		total+=number
	return total 


def get_cube(numbers:list):
	cube = []
	for number in range(1 , 6):
		cube.append(number*number*number)
	return cube	

def get_even_count(value):
	return(len([x for x in value if x%2==0]))

def get_even_count(value):
	return(sum([1 for x in value if x%2 == 0]))		

print(comprehension1())
print(comprehension2())
print(comprehension3())
print(comprehension4())
print(comprehension5())
print(comprehension6())
print(get_even_count([1,5,7,3,2,9,8,10]))










