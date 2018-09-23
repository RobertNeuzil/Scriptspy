import random
"""
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
"""


"""
def choose_a_greeting():
	greeting = ['Hello', 'Hola', "Heeeyyyy", "Hi", "Konnichiwa"]
	which_greeting = random.choice(greeting)
	print (which_greeting)

choose_a_greeting()
choose_a_greeting()
choose_a_greeting()
"""

"""
def roll_of_dice():
	dice = [1, 2, 3, 4, 5, 6]
	choose = random.choices(dice, k=1)
	print (f' Your dice roll was a {choose}')

roll_of_dice()
roll_of_dice()
roll_of_dice()
roll_of_dice()
"""


def roulette_wheel():
	colors = ['red', 'black', 'green']
	choose = random.choices(colors, weights= [18, 18, 2], k=10)
	print (choose)
roulette_wheel()