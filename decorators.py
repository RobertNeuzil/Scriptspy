"""def decorator_func(my_function):

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
display_info("Robert", 55)"""




def my_logger(original_function):
	import logging
	logging.basicConfig(filename=f'{original_function.__name__}', level = logging.INFO)

	def wrapper(*args, **kwargs):
		logging.info(
			f'ran with args {args} and kwargs {kwargs}')

		return original_function(*args, **kwargs)
	return wrapper

def my_timer (original_function):
	import time
	def wrapper(*args, **kwargs):
		t1 = time.time()
		result = original_function(*args, **kwargs)
		t2 = time.time() - t1
		print (f"{original_function} ran in {t2} seconds")
	return wrapper


import time


@my_logger
@my_timer
def display_info(name, age):
	time.sleep(2)
	print (f"The name is {name} and the age is {age}")

display_info("Robert", 27)
display_info("Breanna", 78)
display_info("Alicia", 17)
display_info("Jason", 4)














