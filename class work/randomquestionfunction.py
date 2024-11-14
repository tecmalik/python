import random
passescounter = 0
counter = 0
passes = 0
gen1 = 0
gen2 = 0
sum = 0
answer = []
sign = ["*,-,-,+,+,"]

while(counter<=10):
	gen1 = random.randrange(1,1000)
	gen2 = random.randrange(1,1000)
	for a in "*--++" :
		answer = input(f"what is the sum of this numbers {gen1} {a} {gen2} ?")
		counter+=1
	sum = gen1+gen2
	if answer == sum :
		passescounter+=1
		
	