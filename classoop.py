class Employee():
	
	def __init__(self, first, last, pay, car, shirt):
		self.first = first
		self.last = last
		self.pay = pay
		self.car = car
		self.shirt = shirt
		self.email = f"{first}.{last}@yahoooooo.com"
	def description(self):
		print (f"{self.first} {self.last} makes ${self.pay} dollars a year and drive a {self.car}")

	def give_pay_raise(self):
		self.pay = self.pay * 1.23
	def get_email(self):
		print (f"You can contact {self.first} {self.last} at {self.email}")


emp_1 = Employee("Robert", "Neuzil", 94000, "Ford", "Brown")
emp_2 = Employee("Jessica", "Jones", 80000, "Nissan", "Blue")
emp_3 = Employee("Jacob", "Cross", 5000000000000, "Honda", "Brown")
emp_4 = Employee("Tony", "Soprano", 50000, "GM", "Red")
emp_5 = Employee("Angela", "Mason", 2099999, "Toyota", "Yellow")
emp_6 = Employee("James", "Smith", 444444, "Ford", "Blue")
emp_7 = Employee("Jessica", "Long", 833849384, "Ford", "Grey")
emp_8 = Employee("Robert", "Neuman", 58993849, "Ford", "Purple")

all_employees = [emp_1, emp_2, emp_3, emp_4, emp_5, emp_6, emp_7, emp_8]

for x in all_employees:
	x.description()
for y in all_employees:
	y.give_pay_raise()
	y.description()

emp_3.get_email()

""" PRINTED TO THE CONSOLE:

Robert Neuzil makes $94000 dollars a year and drive a Ford
Jessica Jones makes $80000 dollars a year and drive a Nissan
Jacob Cross makes $5000000000000 dollars a year and drive a Honda
Tony Soprano makes $50000 dollars a year and drive a GM
Angela Mason makes $2099999 dollars a year and drive a Toyota
James Smith makes $444444 dollars a year and drive a Ford
Jessica Long makes $833849384 dollars a year and drive a Ford
Robert Neuman makes $58993849 dollars a year and drive a Ford


-------------------------------AFTER PAY RAISE METHOD -----------------------



Robert Neuzil makes $115620.0 dollars a year and drive a Ford
Jessica Jones makes $98400.0 dollars a year and drive a Nissan
Jacob Cross makes $6150000000000.0 dollars a year and drive a Honda
Tony Soprano makes $61500.0 dollars a year and drive a GM
Angela Mason makes $2582998.77 dollars a year and drive a Toyota
James Smith makes $546666.12 dollars a year and drive a Ford
Jessica Long makes $1025634742.3199999 dollars a year and drive a Ford
Robert Neuman makes $72562434.27 dollars a year and drive a Ford
You can contact Jacob Cross at Jacob.Cross@yahoooooo.com
"""

