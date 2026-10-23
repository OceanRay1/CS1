#Author: Roshan Shivnani
#Date: 10/23/2026
#Purpose/Description: test the methods of counter to see if working
#File: timerdriver.py
#Course: CS1

from counter import Counter

#Creates an object of the class counter
test1 = Counter(limit=60, initial=1, min_digits=2)
print(test1.get_value())
print(test1.__str__())

#Tests the tick feature goes down one
test1.tick()
print(test1.__str__())

#Checks that value loops (back to limit - 1) happens when 0 hit so no negative
test1.tick()
print(test1.__str__())

test2 = Counter(limit = 16, initial=1, min_digits=2)