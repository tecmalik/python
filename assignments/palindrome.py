
integer = int(input("Enter a 3 digit integer :"))
digitOne = integer% 10
digitTwo = (integer//10) % 10
digitThree = (integer//100) % 10 
if digitOne == digitThree:
   	print("The number is a palindrome")

if digitOne != digitThree:
    	print("The number is not a palindrome")
	