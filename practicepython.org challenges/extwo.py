"""
Ask the user for a number. Depending on whether the number is even or odd, print 
out an appropriate message to the user. 
Hint: how does an even / odd number react differently when divided by 2?

"""

num = int(input("Please enter a number:")) 
if num % 2 == 0:  #modulus op will see if there are any dividedends to this number
	print ("Your number is even")
else:
	print ("Your number is odd")

