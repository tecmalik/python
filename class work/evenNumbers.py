initial_point = int(input("Enter initial range: "))
finish_point = int(input("Enter finishing  range: "))
given_value = int(input("Enter given value: "))

count_number = 0

for numbers in range (initial_point, finish_point + 1):
	if numbers % given_value == 0:
		count_number +=1
print(count_number)