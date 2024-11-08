#wright a function sum_of_even_numbers that takes an integer n and returns the sum of all #even numbers from 1 to n.
#Example: sum_of_even_numbers(10).  output: 30(2 + 4 + 6 + 8 + 10 = 30) 

def sum_of_even_numbers(number):
	answer = 0
	for count in range (1 ,number, 2):
		answer+=count
	return(answer)


number = int(input("Enter a number :"))
sum_of_even_numbers(number) 
print(answer)