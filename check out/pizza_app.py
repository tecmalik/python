
		
def menu():
	print("Welcome to Iya Moses joint Ajegunle.")
	print(" -------------------------------------------------")
	print(" |  pizza Type | number of slice | price per box  |")
	print(" |  sapa size  | 4	       | 2,500		  |")
	print(" |  small money| 6	       | 2,900		  |")
	print(" |  big boys   | 8	       | 4,000		  |")
	print(" |  Odogwu     | 12	       | 5,200		  |")
	print(" -------------------------------------------------")
	
	
def pizzaOrder():
	pizzaType = input("Enter pizza type : ")
	if pizzaType.lower() == "sapa size":
		numberOfGuest = int(input("Enter the number of Guest you have : "))
		numberOfSapaPizzaBoxes = int(input("How many Box of Sappa pizza : "))
		print(f"Number of boxes of pizza to buy = {numberOfSapaPizzaBoxes}boxes")
		if numberOfGuest < numberOfSapaPizzaBoxes*4 :
			print(f"Sapa size contains 4 slices per box, {numberOfSapaPizzaBoxes} boxes should be sufficient for {numberOfGuest} persons as it would contain { 4*numberOfSapaPizzaBoxes } slice in all")
			result1 = numberOfSapaPizzaBoxes*4 - numberOfGuest
			print(f"Number of left over sclice after serving = {result1}")
		else:
			print(f"Sapa size contains 4 slices per box, {numberOfSapaPizzaBoxes} boxes should not be sufficient for {numberOfGuest} persons as it would contain {4*numberOfSapaPizzaBoxes} slice in all")
			result2 = numberOfGuest-numberOfSapaPizzaBoxes*4
			print(f" slice will be short with {result2}")  
			
	elif pizzaType.lower() == "small money" :
		numberOfGuest = int(input("Enter the number of Guest you have : "))
		numberOfsmallmoneyBoxes = int(input("How many Box of small money pizza : "))
		
		print(f"Number of boxes of pizza to buy = {numberOfsmallmoneyBoxes}boxes")
		if numberOfGuest < numberOfsmallmoneyBoxes*6 :
			print(f"Small money size contains 6 slices per box, {numberOfsmallmoneyBoxes} boxes should be sufficient for { numberOfGuest} persons as it would contain { 6*numberOfsmallmoneyBoxes } slice in all")
			result1 = numberOfsmallmoneyBoxes*6 - numberOfGuest
			print(f"Number of left over sclice after serving = {result1}")
		else:
			print(f"Small money size contains 6 slices per box, {numberOfsmallmoneyBoxes} boxes should not be sufficient for {numberOfGuest} persons as it would contain { 6*numberOfsmallmoneyBoxes} slice in all")
			result2 = numberOfGuest-numberOfsmallmoneyBoxes*6
			print(f" slice will be short with {result2}")

	elif pizzaType.lower() == "big boys":
		numberOfGuest = int(input("Enter the number of Guest you have : "))
		numberOfbigboysBoxes = int(input("How many Box of big boys pizza : "))
		print(f" Number of boxes of pizza to buy = {numberOfbigboysBoxes}boxes")
		if numberOfGuest < numberOfbigboysBoxes*8 :
			print(f"Bigboy size contains 8 slices per box, {numberOfbigboysBoxes} boxes should be sufficient for {numberOfGuest} persons as it would contain {8*numberOfbigboysBoxes} slice in all")
			result1 = numberOfbigboysBoxes*8 - numberOfGuest
			print(f"Number of left over sclice after serving = {result1}")
		else:
			print(f"Big boy size contains 8 slices per box, {numberOfbigboysBoxes} boxes should not be sufficient for {numberOfGuest} persons as it would contain {8*numberOfbigboysBoxes} slice in all");
			result2 = numberOfGuest-numberOfbigboysBoxes*8
			print(f" slice will be short with {result2}")

	elif pizzaType.lower() == "odogw":
		numberOfGuest = int(input("Enter the number of Guest you have : "))
		numberOfOdogwBoxes = int(input("How many Box of Odogw pizza : "))
		print(f"Number of boxes of pizza to buy = {numberOfOdogwBoxes}boxes")
		if numberOfGuest < numberOfOdogwBoxes*12 :
			print(f"Odogwu size contains 12 slices per box, {numberOfOdogwBoxes} boxes should be sufficient for {numberOfGuest} persons as it would contain {12*numberOfOdogwBoxes} slice in all")
			result1 = numberOfOdogwBoxes*12 - numberOfGuest;
			print(f"Number of left over sclice after serving = {result1}")
		else:
			print(f"Odoguw size contains 12 slices per box, {numberOfOdogwBoxes} boxes should not be sufficient for {numberOfGuest} persons as it would contain {12*numberOfOdogwBoxes} slice in all")
			result2 = numberOfGuest-numberOfOdogwBoxes*12
			print(f" slice will be short with {result2}")

menu()
pizzaOrder()