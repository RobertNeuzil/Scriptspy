def square(num):
	return num * num

def my_map(func, arg_list):
	result = []
	for i in arg_list:
		result.append(func(i))
	return result

squares_fcf = my_map(square, [3, 9, 11, 20, 49])

print (squares_fcf)




