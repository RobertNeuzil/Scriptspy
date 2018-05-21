def playgame():

	playerone = input("Please enter rock, paper or scissors:")
	playertwo = input("Please enter rock, paper or scissors:")
	playerone.lower()
	playertwo.lower()

	if playerone == playertwo:
		print ("tie game")
	elif playerone == "rock":
		if playertwo == "scissors":
			print ("rock wins")
		elif playertwo == "paper":
			print ("paper wins")
	elif playerone == "paper":
		if playertwo == "rock":
			print ("paper wins")
		if playertwo == "scissors":
			print ("scissors wins")
	elif playerone == "scissors":
		if playertwo == "rock":
			print ("rock wins")
		if playertwo == "paper":
			print ("scissors wins")
