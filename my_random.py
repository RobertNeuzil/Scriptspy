import random
import os
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

"""
def roulette_wheel():
	colors = ['red', 'black', 'green']
	choose = random.choices(colors, weights= [18, 18, 2], k=10)
	print (choose)
roulette_wheel()
"""
"""
deck = list(range(1, 53))
random.shuffle(deck)
hand = random.sample(deck, k=5)

print (hand) 
"""

first_names = ['John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam', 'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe', 'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara', 'Elizabeth', 'Laura', 'Jennifer', 'Maria']

last_names = ['Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart', 'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks', 'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown', 'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris', 'Martin']

street_names = ['Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak', 'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill']

fake_cities = ['Metropolis', 'Eerie', "King's Landing", 'Sunnydale', 'Bedrock', 'South Park', 'Atlantis', 'Mordor', 'Olympus', 'Dawnstar', 'Balmora', 'Gotham', 'Springfield', 'Quahog', 'Smalltown', 'Epicburg', 'Pythonville', 'Faketown', 'Westworld', 'Thundera', 'Vice City', 'Blackwater', 'Oldtown', 'Valyria', 'Winterfell', 'Braavos‎', 'Lakeview']

states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

for num in range(1500):



	first = random.choice(first_names)
	last = random.choice(last_names)
	street = random.choice(street_names)
	city = random.choice(fake_cities)
	the_state = random.choice(states)

	all_info = f'{first} {last} lives on {street} ST. in the city of {city} which is located in {the_state}.\n'
	
	
	x = 1

	while x <= 1:
		x += 1
		f = open("allinforandommodule.txt", "a+", encoding='utf-8')
		f.write(all_info)
		f.close()
	

