import random
randnum = random.randrange(1, 10) #choose random number
print ("Please guess a number between 1 and 9 in 3 guesses or less")

x = 0
# print (randnum)
while x < 3:  # only allows three guesses
	usenum = int(input("Please enter an integer:"))
	if x == 2:  # starts at zero, x == 0 is guess one.
		print ("I'm sorry, you have run out of guesses")
		break # by the time x is == 2, there is no reason to continue loop
	elif usenum == randnum:
		print ("Congratulations you guessed correctly")
		break # no reason to continue loop if guess is right
	elif usenum < randnum:
		x += 1 # adds to x variable for new guess
		print ("I'm sorry, that number is not correct, please try again")
		continue # will run while x < 3, x != 2, and usenume != randnum evaluates to True 
	


