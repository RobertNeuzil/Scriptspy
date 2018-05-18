class Employee():

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay

	def fullname(self):
		return f"{self.first} {self.last} is the full name"

	def apply_raise(self):
		self.pay = self.pay * 1.07



class SpecialEmployee(Employee):
	def __init__(self, first, last, pay, specialskill):
		super().__init__(first, last, pay)
		self.specialskill = specialskill
	
	def apply_raise(self):
		self.pay = self.pay * 7.50




emp_1 = Employee("Allan", "Tucker", 56000)
emp_2 = Employee("Eric", "White", 64000)
emp_3 = SpecialEmployee("Jessica", "Jones", 62000, "block mind control")
emp_4 = SpecialEmployee("Luke", "Cage", 60000, "superhuman strength")

print (emp_3.pay)
emp_3.apply_raise()
print (int(emp_3.pay))
print (emp_4.pay)




