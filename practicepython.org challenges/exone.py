"""
Create a program that asks the user to enter their name and their age. Print out 
a message addressed to them that tells them the year that they will turn 100 years old.

"""

from datetime import datetime  #module to get current year

name = input ("Please enter your name:")
age = input("Please enter your age:")

subtract = 100 - int(age)  
currentYear = datetime.now().year # calling date time module here
hundred = currentYear + subtract

print (f"Hello {name}, you will turn 100 in the year {str(hundred)}") # formatting print to include applicable variables


