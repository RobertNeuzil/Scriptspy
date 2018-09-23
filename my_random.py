import random

def roll_of_dice():
	roll = random.randint(0, 6)
	if roll == 1:
		print ("The dice came up one")
	elif roll == 2:
		print ("The dice came up two")
	elif roll == 3:
		print ("The dice came up three")
	elif roll == 4:
		print ("The dice came up four")
	elif roll == 5:
		print ("The dice came up five")
	else:
		print ("The dice is a six")
roll_of_dice()
roll_of_dice()
roll_of_dice()
roll_of_dice()