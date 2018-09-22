def decorator_func(my_func_test):
	
	def wrapper_func():
		print (f"wrapper is executing this before executing {my_func_test.__name__}")
		
		
		return my_func_test()

	return wrapper_func



@decorator_func
def test():
	print ("The test worked!")

@decorator_func
def test_again_twice():
	print ("The test worked a second time")

test()
test_again_twice()
