while milesdriven != -1:
	milesdriven =int(input("Enter the miles driven or -1 t0 exit : "))
	numberOfgallons = int(input("Enter the number of gallons used or -1 t0 exit : "))
	milespergallon = (float)milesdriven / (float)numberOfgallons;
	print(f"the miles per gallon is {milespergallon}")