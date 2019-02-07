	import random

	randominteger = random.randint(1,10)
	attempts = 1

	userName = input("Hi! What is your user name?")

	print("Hello" , userName + "." , )

	question = input("Would you like to play a game ? [Y/N] " )
	if question == "N":
	print ("Well that's mean")
	
	if question == "Y":
		print("I'm thinking of a number between 1 and 10")
		guess = int(input("Try it: "))
		if guess > randominteger: #if user's entry is greater to the random number, denote failure
			print("Guess lower")
		if guess < randominteger: #if user's entry is lower to the random number, denote failure
			print("Go higher") 
		while guess != randominteger: #With each attempt, you try again and the attempts are incremented
			attempts += 1
			guess = int(input("Yo you messed up yo, try again:  "))
		if guess == randominteger: #if user's entry is equal to the random number, denote success
			print("You got it! The integer was", randominteger, "and it only took", attempts, "attempts!" , " NOW GO DO SOMETHING PRODUCTIVE WITH YOU LIFE ")
			
	