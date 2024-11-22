import random
passescounter = 0
counter = 0
passes = 0
failures = 0
gen1 = 0
gen2 = 0
sum = 0
useranswer = 0
correction = []
correction2 = []
correction3 = []

while(counter<10):
	if counter<5:
		gen1 = random.randrange(1,1000)
		gen2 = random.randrange(1,1000)
		useranswer = int(input(f"what is the sum of {gen1} + {gen2} ? : "))
		realanswer = gen1+gen2
		correction.append(f"{gen1} + {gen2} = {realanswer} your input was {useranswer}")
		counter+=1
		if useranswer == realanswer:
			passes+=1 
		else:
			failures+=1

	if counter<8:
		gen1 = random.randrange(1,1000)
		gen2 = random.randrange(1,1000)
		useranswer = int(input(f"what is the subtraction of {gen1} - {gen2} ? : "))
		realanswer2 = gen1-gen2
		correction2.append(f"{gen1} - {gen2} = {realanswer2} your input was {useranswer}")
		counter+=1
		if useranswer == realanswer:
			passes+=1 
		else:
			failures+=1


	if counter<10:
		gen1 = random.randrange(1,1000)
		gen2 = random.randrange(1,1000)
		useranswer = int(input(f"what is the product of {gen1} X {gen2} ? : "))
		realanswer3 = gen1*gen2
		correction3.append(f"{gen1} * {gen2} = {realanswer3} your input was {useranswer}")
		counter+=1

		if useranswer == realanswer:
			passes+=1 
		else:
			failures+=1

for i in correction:
	print(i)
for i in correction2:
	print(i)
for i in correction3:
	print(i)
print(f"the number of passes are {passes}")
print(f"the number of failures failures are {failures}")
print(f"grade = {passes} / {failures}")