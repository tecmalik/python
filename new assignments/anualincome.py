
annualIncome = int(input(" Enter Annual income  :"))
tax = 0
if annualIncome < 9875 :
	tax = float((annualIncome/100)*10)
	print(f"TAX RATE based on 10% is {tax}")
elif annualIncome >= 9876 and annualIncome <=40125 :
	tax = float((annualIncome/100)*12)
	print(f"TAX RATE is 12 % is {tax}")
elif (annualIncome >= 40126 and annualIncome <=185525 ):
	tax = float((annualIncome/100)*22)
	print(f"TAX RATE 22 % is {tax}" )
elif (annualIncome >= 85525 ):
	tax = float((annualIncome/100)*24)
	print(f"TAX RATE 24 % is {tax}")