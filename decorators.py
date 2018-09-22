def outer_func(msg):

	def inner_func(msgtwo):
		print (msg + msgtwo)
	return inner_func

grand = outer_func("Hi")
grand(" and good morning")
grand(" and good night")
grand(" and good evening")
grand(" and it's lunchtime")
grand(" and it's 5 pm")