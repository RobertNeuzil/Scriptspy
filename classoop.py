class Dog():

	def __init__(self, name, breed, coat):
		self.name = name
		self.breed = breed
		self.coat = coat
		self.email = f"{self.name}@woofwoof.com".lower()
	def do_trick(self):
		self.treats = self.treats + 1

	@classmethod 
	def set_class_amount(cls, treats, animals):
		cls.treats = treats 
		cls.animals = animals

Dog.set_class_amount(333, "dogs") # class methods effects the whole class as opposed to each instance
xyz = Dog("Rodrigo", "Doberman", "White")
lol = Dog("Crayon", "Boxer", "Brown")
nvm = Dog("Scooter", "Pitbull", "White")
abc = Dog("Spot", "Pitbull", "White")
print (xyz.treats)
xyz.do_trick()
print (xyz.treats)
print (lol.treats)
print (nvm.treats)
print (abc.treats)








