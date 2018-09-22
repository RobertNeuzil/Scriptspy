def outer_func(msg):
	

	def inner_func():
		print (msg)

	return inner_func

my_func = outer_func("Hello")
lol = outer_func("Goodbye")

my_func()
lol()

