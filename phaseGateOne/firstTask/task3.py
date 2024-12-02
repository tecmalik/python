firstNumber = int(input("Enter first Number :"))
secondNumber = int(input("Enter second Number :"))
thirdNumber = int(input("Enter third Number :"))
if firstNumber<secondNumber<thirdNumber:
	print(f"{firstNumber},{secondNumber},{thirdNumber}")
elif secondNumber<firstNumber<thirdNumber:
	print(f"{secondNumber},{firstNumber},{thirdNumber}")
elif thirdNumber<secondNumber<firstNumber:
	print(f"{thirdNumber},{firstNumber},{secondNumber}")
elif secondNumber<thirdNumber<firstNumber:
	print(f"{secondNumber},{thirdNumber},{firstNumber}")
elif firstNumber<thirdNumber<secondNumber:
	print(f"{firstNumber},{thirdNumber},{secondNumber}")
elif secondNumber<firstNumber<thirdNumber:
	print(f"{secondNumber},{firstNumber},{thirdNumber}")