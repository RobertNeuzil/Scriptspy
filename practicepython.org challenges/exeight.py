def playgame():  # creating a function to call game
	
	playerone = input("Please enter rock, paper or scissors:")
	playertwo = input("Please enter rock, paper or scissors:")
	playerone.lower() # makes it simpler to compare strings in variables
	playertwo.lower()
	
	if str(playerone) == str(playertwo): 
		print ("tie game")
	elif str(playerone) == "rock": # player one entered rock
		if str(playertwo) == "scissors":
			print ("rock wins")  
		elif str(playertwo) == "paper":    # wins or loses, according to game rules
			print ("paper wins")
	elif str(playerone) == "paper":   # player one entered paper
		if str(playertwo) == "rock":
			print ("paper wins")
		if str(playertwo) == "scissors":
			print ("scissors wins")
	elif str(playerone) == "scissors":
		if str(playertwo) == "rock":
			print ("rock wins")
		if str(playertwo) == "paper":
			print ("scissors wins")
	else:
		print ("your entry was not valid. Please play again")

# no loop needs to be created for player two. He/She are already accounted for in their possible
# choices within the if/else for player one. 