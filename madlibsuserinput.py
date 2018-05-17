adjective = input ("please enter an adjective:")
adjectivetwo = input("please enter another adjective:")
adjectivethree = input("please enter another adjective:")
color = input("please enter a color:")
verb = input("please enter a verb:")
place = input("please enter a place:")
planet = input("please enter a planet:")
task = input("please enter a task:")
try:
        number = int(input("please enter a number:"))
        
except ValueError:
        number = int(input("please enter an integer:"))
else:
        number = 2
       

print (f"""
The meatballs at our school are very {adjective}. They look very {color} and taste very 
{adjectivetwo}. Last week, I swore I saw one get up and {verb}! They must come from {place}.
If I didn't know better, I would say they were from {planet}! Before long, one of them is going to learn how
to {task}. Then we will all be in trouble! I give it less than {int(number)} days.


""")
	
