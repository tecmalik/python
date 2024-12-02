from datetime import datetime
	
		
def femalesPlan():
	userAge = int(input("Enter your Age :"))
	cyclelength = int(input("Enter the length of your cycle e.g 28/27 days: "))
	int periodDuration = int(input("Enter period duration:\n e.g 4/7 "))
	lastPeriodDate = input("Enter the date of the first day of your last period using \"yyyy-mm-dd\" format : ")
		
	lastDate = datetime.strptime(lastPeriodDate)	
	nextPeriodStart = lastDate - timedelta(days =cyclelength)
		
	nextLastDayofBleeding = nextPeriodStart + timedelta(days =periodDuration)
		
	nextEndofCycleDate =  nextPeriodStart + timedelta(cyclelength+1)
	nextOvulationDate =  nextEndofCycleDate - timedelta(days =14)
	safePeriod3 = nextOvulationDate + timedelta(days =1)
	safePeriod4 = nextOvulationDate + timedelta(days =7)
	safeperiod1 = nextLastDayofBleeding + timedelta(days =1)
	safeperiod2 = nextLastDayofBleeding + timedelta(days = 7)
		
	print(" your next End of Cycle Date"+nextEndofCycleDate)
	print(" your next Last Day of Bleeding"+nextLastDayofBleeding)	
	print(" your next Period starts on "+ nextPeriodStart)
	print(" your next end of cucledate Date is "+nextEndofCycleDate)
	print(" your next Safe Period before ovulation starts"+safeperiod1)
	print(" your next Safe Period before ovulation ends"+safeperiod2)
	print(" your next Ovulation date is "+nextOvulationDate)
	print(" your next Safe Period after ovulation starts "+safePeriod3)
	print(" your next Safe Period after ovulation ends "+safePeriod4)
	
def gender():
	gender = int(input("Sellect Gender:   \n1. male \n2. female \n"))
	match gender :
		case 1 :isMale()
		case 2 :femalesPlan()
		case _ : print("invalid input")
			gender();			

def isMale():
	option = int(input(" want to keep track \n1. with your partners period \n2. with your partner mood ?"))
	match option:
		 
		case 1: 
			print("enter her code"); 
		case 2:
			 print("enter her code");
		case_ : print("invalid input")
			gender();


username = input("Enter your name :")
print("welcome to the Menstrual app ")
gender()
	
