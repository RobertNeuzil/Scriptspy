"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that 
are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.


"""

# THIS WAS EXPANDED ON AND COMMENTED THROUGH IN EXC 10


a = [1, 4, 5, 8, 9, 10, 11, 14, 44, 55]
b = [1, 2, 3, 4, 5, 6, 8]
a.extend(b)
a.sort()
c = set(a)
d = list(c)
print (d)