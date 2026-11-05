#Author: Roshan Shivnani
#Date: 11/04/2026
#Purpose/Description: implementing binary search recursively
#File: binary_search.py
#Course: CS1

#COPIED DRIVER FILE FROM ASSIGNMENT AND ADDED BINARY SEARCH FUNCTION
from random import randint

# Perform binary search for key on the sublist of the_list
# starting at index left and going up to and including index right.
# If key appears in the_list, return the index where it appears.
# Otherwise, return None.
# Requires the_list to be sorted.

def binary_search(the_list, key, left=None, right=None):
    # If using the default parameters, then search the entire list.
    if left == None and right == None:
        left = 0
        right = len(the_list) - 1

    #if left ever greater than right and item not found then not in list
    if left > right:
        return None

    #calculates the middle index of the two pointers
    mid_i = (left + right) // 2

    #return the index of the key if it is found
    if key == the_list[mid_i]:
        return mid_i

    #if the key is less than the middle of the list cap upper bound to middle of list
    #also go one term below mid since you know mid isn't key since previously checked
    if key < the_list[mid_i]:
        return binary_search(the_list, key, left, mid_i - 1)

    #if the key is more than the middle of the list cap lower bound to middle of list
    #also go one term above mid since you know mid isn't key since previously checked
    if key > the_list[mid_i]:
        return binary_search(the_list, key, mid_i + 1, right)

# Driver code for binary search.
n = int(input("How many items in the list? "))

# Make a list of n random ints.
i = 0
the_list = []
while i < n:
    the_list.append(randint(0, 1000))
    i += 1

# Binary search wants a sorted list.
the_list = sorted(the_list)
print("The list: " + str(the_list))

while True:
    key = input("What value to search for? ('?' to see the list, 'q' to quit): ")

    if key == "?":
        print("The list: " + str(the_list))
    elif key == "q":
        break
    else:
        key = int(key)
        index = binary_search(the_list, key)
        if index == None:
            print(str(key) + " not found")
        else:
            print(str(key) + " found at index " + str(index))