counter = 1
numberofpasses = 0
numberoffailures = 0
while counter < 16:
	grade = int(input("Enter student Grade :"))
	counter += 1
	if grade > 45:
		numberofpasses += 1
	elif grade < 45 :
		numberoffailures += 1
		
	if grade > 45 :
		
		print("student passed")
	else :
		print("student failed")
print(f" number  0f passes {numberofpasses} \n number of failires{numberoffailures}")