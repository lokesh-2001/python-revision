# Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.
# Extras:
# Randomly generate two lists to test this
# Write this in one line of Python 

print(list(set(a) & set(b)))
print()
print(list(set(a).intersection(b)))
print()
print(list(filter(lambda x: x in a,b)))
print()

import numpy as np
print(list(np.intersect1d(a,b)))
print()
result = []
for i in a:
    if i in b:
        result.append(i)

print(result)