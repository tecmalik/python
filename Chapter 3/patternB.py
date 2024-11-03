print("Pattern A")
for a in range(1, 7):
	for b in range(1, a + 1 ):
		print("*", end="")
	print()
		 
print("Pattern B")
for x in range(1, 7):
	for y in range(6, x - 1, -1): 
		print("*", end="")
	print()
print("Pattern C")
for m in range(1, 7):
	for z in range (1, 7 - m):
		print(" ", end="")
	for n in range(1, m + 1):
		print("*", end="")
	print()
		  
print("Pattern D")
for c in range(1, 7):
	for k in range(1, c):
		print(" ",end="")
	for i in range(1, 7):
		print("*",end="")
	print()
	  	