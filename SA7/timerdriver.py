#Author: Roshan Shivnani
#Date: 10/23/2026
#Purpose/Description: test timer given 1 hour 30 min clock
#File: timerdriver.py
#Course: CS1

from timer import Timer

#prints timer starting at 1:30:00 before ticking
print(my_timer)

#runs until the timer hits 00:00:00 while printing each seconds (tick)
while my_timer.is_zero() == False:
    my_timer.tick()
    print(my_timer)

