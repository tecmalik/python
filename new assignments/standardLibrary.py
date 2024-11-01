daysNumber = 0
counterNumber = 0
		
while counterNumber < 3:
	daysNumber = int(input("Enter number of days"))
	++counterNumber
	if daysNumber <5 :
		print(" Payment is 0 Payment ")
			
	if daysNumber == 5:
		print(" pay 50 paise ")
		
	elif  daysNumber >= 6 and daysNumber <= 10: 
		print(" Pay 1 rupees ")
		
	elif  daysNumber > 10 and daysNumber < 30:
		print(" Pay 5 rupees ")

	elif daysNumber > 30:
		print(" membership will be Cancelled ")
		 