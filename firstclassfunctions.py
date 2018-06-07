
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


######################################################################################################decorators######


def decorator(f):  # the decorator needs an implicit argument that will serve as the function you're calling in the nested wrapper function

	def wrapper(*args):
		print ("Before function called")
		f(*args)
		print ("After function called")
	return wrapper # no parentheses because that would execute function. Only looking to return the wrapper function
	#within the decorator in order to later pass in f() and then execute wrapper + f() together, at once. They will all be
	# executed when the decorated function is called


@decorator
def printname(name):
	print (name)

printname("Robert")







