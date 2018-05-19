class Dog():

	def __init__(self, name, breed, coat):
		self.name = name
		self.breed = breed
		self.coat = coat
		self.email = f"{self.name}@woofwoof.com".lower()
	
	def __repr__(self):
		return f"{self.name}, {self.breed}, {self.coat}"
	def __str__(self):
		return f"{self.name} - {self.breed} - {self.email}"

	def do_trick(self):
		self.treats = self.treats + 1


dog_1 = Dog("Roscoe", "Doberman", "White")
dog_2 = Dog("Angel", "Pitbull", "Black")

print (dog_1)

print (repr(dog_1))
print (str(dog_1))