#Author: Roshan Shivnani
#Date: 10/23/2026
#Purpose/Description: test timer given 1 hour 30 min clock
#File: timerdriver.py
#Course: CS1

from timer import Timer

#Starts the 1 hour 30 minute timer the assignment asks for
my_timer = Timer(hours=1, minutes=30, seconds=0)

#Runs until the timer hits 00:00:00
while str(my_timer) != "00:00:00":
    my_timer.tick()
    print(my_timer)
