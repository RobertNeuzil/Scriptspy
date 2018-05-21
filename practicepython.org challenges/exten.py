"""
This week’s exercise is going to be revisiting an old exercise (see Exercise 5), 
except require the solution in a different way.

Take two lists, say for example these two:

	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


"""



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] # two lists
mylist = [num for num in a] + [num for num in b] # joining two lists together with list comp
mylist.sort() # ordering list in order with list method sort
myset = set(mylist) # converting to a set in order to see no value repeating
newlist = list(myset) #converting back to a list 
print (newlist)
