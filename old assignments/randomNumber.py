import random
randomNumber = random.randint(1,100)
randomGuess = 0
while randomGuess != randomNumber:
	randomGuess = int(input("Enter a number between 1  to 100 number :"))
	if randomGuess > randomNumber :
		print("too high, try again.")
	elif randomGuess < randomNumber :
		print("too low, try again.")
	else :
		print("success !, You guessed right.")
	