
number = 0
while number != -1 :
	noofgallon = float(input("Enter the gallons used (-1 to end): "))
	if noofgallon == -1 :
		break
	milesdriven = float(input("Enter the miles driven: "))
	
	milespergallon =  milesdriven / noofgallon
	print("The milespergallon for this tank was",milespergallon)
	