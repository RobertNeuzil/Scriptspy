
def hello(x):      #create a function
	return x * x # returns a square

def goodbye (func, args_list):  #takes the argument of function and a list
	new = [] # will return new list after
	for i in args_list: # loop through every number in arg_list
		new.append(func(i)) # append it to new after the numbers in arg list are run through the func
	return new

squares = goodbye(hello, [1, 2, 3, 4, 5]) 
print (squares)



def trythis(x):

	def text_wrapper(y):
		print (f"{x} {y} {y} {x}")
	return text_wrapper

something = trythis("Something") #something has now been committed to memory to keep the "Something" argument for try this over and over again
something("middle")
something("car")

