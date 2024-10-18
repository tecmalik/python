firstDigit = int(input('First number number :'))
secondDigit = int(input('Second number :'))
thirdDigit = int(input('third number :'))
if (firstDigit > secondDigit and firstDigit > thirdDigit):
	print('the largest  number is' , firstDigit)
if (secondDigit > firstDigit and secondDigit > thirdDigit):
	print('the largest  number is' , secondDigit)
if (thirdDigit > firstDigit and thirdDigit > secondDigit ):
	print('the largest  number is' , secondDigit)
if (firstDigit < secondDigit and firstDigit < thirdDigit):
	print('the smallest  number is' , firstDigit)
if (secondDigit < firstDigit and secondDigit < thirdDigit):
	print('the smallest  number is' , secondDigit)
if (thirdDigit < firstDigit and thirdDigit < secondDigit ):
	print('the smallest  number is' , secondDigit)
sum = firstDigit + secondDigit + thirdDigit
average = (firstDigit + secondDigit + thirdDigit)/3
product = firstDigit * secondDigit * thirdDigit
print('sum is',sum)
print('average is',average)
print('product is',product)