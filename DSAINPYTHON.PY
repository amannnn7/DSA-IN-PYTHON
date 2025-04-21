
# for doing data structures and algorithms in Python
# while writing code in python we have to import the built in function of the python 
# for example import random, etc.
# import math

#ARRAY

# from array import *
# a1 = array('i', [0, 1, 2, 3, 4, 5])
# print(a1)
# print(a1[2])  # Accessing the third element of the array
# a1.append(6)
# a1.insert(0, 0)  # Inserting 0 at the beginning of the array
# #now if we want to print single single element so for that we use for loop
# for element in a1:
#     print(element)
# output 
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# we can also write like 
# for element in range(5):
#     print(a1[element], end=' ')


#now using while loop
# i = 0
# while i < len(a1):
#     print(a1[i])
#     i += 1

#output
# 0
# 1
# 2
# 3
# 4
# 5

#different aaray methods in python
# 1. append(value): Adds a new element at the end of the array.
# 2. insert(index, value): Inserts a new element at a specified index in the array.
# 3. remove(value): Removes the first occurrence of a specified value from the array.
# 4. pop(index): Removes and returns the element at the specified index from the array.
# 5. index(value): Returns the index of the first occurrence of a specified value in the array.
# 6. extend(iterable): Adds elements from an iterable (like a list) to the end of the array.
# 7. count(value): Returns the number of occurrences of a specified value in the array.
# 8. reverse(): Reverses the order of the elements in the array.
# 9. slice(start, end): Returns a new array containing the elements from the specified start index to the end index (exclusive).
# 10. copy(): Returns a shallow copy of the array.
# 11. clear(): Removes all elements from the array.
# 12. sort(): Sorts the elements of the array in ascending order.
# 13. insert_multiple(index, values): Inserts multiple new elements at a specified index in the array.
# 14. tolist(): Converts the array to a regular Python list.
# 15. find(value): Returns True if the specified value is found in the array, otherwise returns False.
# 16. unique(): Returns a new array containing only unique elements from the array.

# Example usage of array methods in Python
# Creating an array
from array import array
a1 = array('i', [0, 1, 2, 3, 4, 5, 6])
# Using the append method to add a new element to the array
a1.append(7)
# Using the insert method to add a new element at index 0\na1.insert(0, -1)
# Using the remove method to remove the first occurrence of the value 3
a1.remove(3)
# Using the pop method to remove and return the last element of the array\nremoved_element = a1.pop()
# and if we signify the index number then it will pop that number only from the respective index place
# Using the index method to find the index of the value 2\nindex_of_2 = a1.index(2)
# Using the extend method to add multiple elements at once\na1.extend([8, 9, 10])
print(a1)