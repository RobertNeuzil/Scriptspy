def playgame():  # creating a function to call game

	playerone = input("Please enter rock, paper or scissors:")
	playertwo = input("Please enter rock, paper or scissors:")
	playerone.lower() # makes it simpler to compare strings in variables
	playertwo.lower()

	if playerone == playertwo: 
		print ("tie game")
	elif playerone == "rock": # player one entered rock
		if playertwo == "scissors":
			print ("rock wins")  
		elif playertwo == "paper":    # wins or loses, according to game rules
			print ("paper wins")
	elif playerone == "paper":   # player one entered paper
		if playertwo == "rock":
			print ("paper wins")
		if playertwo == "scissors":
			print ("scissors wins")
	elif playerone == "scissors":
		if playertwo == "rock":
			print ("rock wins")
		if playertwo == "paper":
			print ("scissors wins")
# no loop needs to be created for player two. He/She are already accounted for in their possible
# choices within the if/else for player one. 