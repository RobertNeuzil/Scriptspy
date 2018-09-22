def decorator_func(my_function):

	def wrapper_func(*args, **kwargs):

		print (f"This is the wrapper function executiong before {my_function.__name__}")

		return my_function(*args, **kwargs)
	return wrapper_func


@decorator_func
def test():
	print ("This is a test that worked")

@decorator_func
def display_info(name, age):
	print (f"This function is running with the [ {name} ] and [ {age} ] arguments")


test()
display_info("Robert", 55)