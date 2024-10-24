
integer = int(input("Enter a 3 digit integer :"))
digitOne = integer% 10 
digitTwo = (integer//10) % 10 
digitThree = (integer//100) % 10
sumOfDigits = digitOne + digitTwo + digitThree;
print("The sum of the three last Entered digits is:", sumOfDigits)
