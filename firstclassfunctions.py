"""
functions can be passed into other functions in order to carry out multiple operations at once """


def squared(f):
	return f * f

lol = squared

def cubed (f):

	return f * f * f

def subtract (f):

	return f - 3

rofl = subtract

def mapping(myfunc, my_list):
	result = []
	for x in my_list:
		result.append(myfunc(x))
	return result


print (mapping(lol, [5, 10, 15, 100, 105]) )
print (mapping(cubed, [5, 10, 15, 100, 105]))
print (mapping(rofl, [5, 10, 15, 100, 105]))






def logger(msg):

	def printlog():
		print ("log:" + msg)

	return printlog

hitherelog = logger(" Hi")
hitherelog()


def html_tag(tag):

	def write(msg):
		return f'{tag}{msg}{tag}'

	return write

hello_world = html_tag(' </h1> ')
print (hello_world("Hello World"))




