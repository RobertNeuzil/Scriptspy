class Dog():

	animal = "Dog"
	treats = 1

	def __init__(self, name, breed, coat):
		self.name = name
		self.breed = breed
		self.coat = coat
		self.email = f"{self.name}@woofwoof.com".lower()
	def do_trick(self):
		self.treats = self.treats + 1

dog_1 = Dog("Roscoe", "Doberman", "White")
dog_2 = Dog("Angel", "Terrier", "Black")
dog_3 = Dog("Dundy", "Pitbull", "Brown")

print(f"{dog_2.name} gets {dog_2.treats} treat.")
dog_2.do_trick()
print (f"{dog_2.name} did a trick so now she gets {str(dog_2.treats)} treats.")
print(f"{dog_3.name}'s email is {dog_3.email}")