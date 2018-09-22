def decorator_func(my_func_test):
	
	def wrapper_func():
		
		return my_func_test

	return wrapper_func

def test():

	print ("The test worked!")

def test_again():
	
	print("The test worked again")


first = test
second = test_again

first()
second()