class Dog():

	def __init__(self, name, breed, coat):
		self.name = name
		self.breed = breed
		self.coat = coat
		self.email = f"{self.name}@woofwoof.com".lower()
	def do_trick(self):
		self.treats = self.treats + 1

	@classmethod 
	def classassign(cls, house, toy):
		cls.house = house 
		cls.toy = toy

	@staticmethod
	def barkbark ():
		if Dog.toy == True:
			print ("Woof Woof")
		else:
			pass


Dog.classassign(False, True)
lol = Dog("Roscoe", "Doberman", "White")
print (lol.house)
lol.barkbark()









