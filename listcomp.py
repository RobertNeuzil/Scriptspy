mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

mylist = [n for n in mylist]
print (mylist)
mylist = [n * 2 for n in mylist]
print (mylist)
mylist = [n + 2 + n + 13 for n in mylist] # iterates through list and adds two to each number then adds 13 to that sum
print (mylist)
mylist = [n for n in range(1, 3) for n in mylist] #creates new list takes the previous list and loops through it twice range(1, 3) 
print (mylist)
