#Author: Roshan Shivnani
#Date: 11/16/2026
#Purpose/Description: test city object by going through list of wrld cities and using it
#File: quicksort.py
#Course: CS1

#splits the list around a pivot "partitioning" it into 2
def partition(the_list, p, r, compare_func):
    pivot = the_list[r]
    i = p - 1
    for j in range(p, r):
        if compare_func(the_list[j], pivot):
            i = i + 1
            #swaps the_list[j] and the_list[i]
            temp = the_list[j]
            the_list[j] = the_list[i]
            the_list[i] = temp
    #swaps the_list[r] and the_list[i + 1]
    temp = the_list[r]
    the_list[r] = the_list[i+1]
    the_list[i+1] = temp
    return i+1

#implement quicksort algorithm from assignment recursively until list sorted
def quick_sort(the_list, p, r, compare_func):
    if p < r:
        q = partition(the_list, p, r, compare_func)
        quick_sort(the_list, p, q-1, compare_func)
        quick_sort(the_list, q+1, r, compare_func)

#call quicksort function to entire list
def sort(the_list, compare_func):
    if len(the_list) > 1:
        quick_sort(the_list, 0, len(the_list)-1, compare_func)

