secondTaxTotal = 0;
thirdTaxTotal = 0;
		
firstName = input("Enter Citizens Name : ")
firstAmount = float(input("Enter amount of anual earnings : "))
secondName =input("Enter Second Citizens Name : ")
secondAmount =float (input ("Enter Second Citizens amount of anual earnings : "))
thirdName = input("Enter Third Citizens Name : ")
thirdAmount = float(input("Enter Third Citizens amount of anual earnings : "))	
if firstAmount > 30_000:
	firstTaxTotal = firstAmount * 0.20;
else :firstTaxTotal = firstAmount * 0.15;

if secondAmount > 30_000:
	secondTaxTotal = secondAmount * 0.20;
else :
	secondTaxTotal = secondAmount * 0.15;
if thirdAmount > 30_000:
	thirdTaxTotal = thirdAmount * 0.20;

else :
	thirdTaxTotal = thirdAmount * 0.15;

print( "%s tax total is %.3f%n",firstName , firstTaxTotal)
print( "%s tax total is %.3f%n",secondName, secondTaxTotal)
print( "%s tax total is %.3f%n",thirdName, thirdTaxTotal)
