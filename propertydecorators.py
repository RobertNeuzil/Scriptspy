class Dog():

	def __init__(self, first, last, breed, coat):
		self.first = first
		self.last = last
		self.breed = breed
		self.coat = coat
	
	@property	
	def email(self):
		return (f"{self.first}{self.last}@woofwoof.com".lower())

	

dog_1 = Dog("Roscoe", "Bone", "Doberman", "White")

print (dog_1.email)