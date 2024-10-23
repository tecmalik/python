firstinput = float(input("Enter first number: "))
secondinput = float(input("Enter second number: "))
thirdinput = float(input("Enter Third number: "))

if firstinput < secondinput < thirdinput:
	print(firstinput , secondinput , thirdinput) 

elif firstinput < thirdinput < secondnput:
	print(firstinput , thirddinput , secondinput)

elif secondinput < firstinput  < thirdinput:
	print(secondinput , firstinput , thirdinput) 

elif secondinput < thirdinput  < firstinput:
	print(secondinput , thirdinput , firstinput) 

elif thirdinput < firstinput < secondinput:  
	print(thirdinput , firstinput , secondinput) 
else:
	print(firstinput, thirdinput, secondinput)
