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

#creates second object of class counter
test2 = Counter(limit = 16, initial=14, min_digits=3)

#same tests as test 1 on this counter test2
print(test2.get_value())
print(test2.__str__())

#tests the tick feature goes down one
test2.tick()
print(test2.__str__())
