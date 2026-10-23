#Author: Roshan Shivnani
#Date: 10/23/2026
#Purpose/Description: make a timer class using counter class
#File: timer.py
#Course: CS1

from counter import Counter

class Timer():

    def __init__(self, hours, minutes, seconds):
        self.hours = Counter(limit=60, initial=hours, min_digits=2)
        self.minutes = Counter(limit=60, initial=minutes, min_digits=2)
        self.seconds = Counter(limit=60, initial=seconds, min_digits=2)

    def __str__(self):
        time = str(self.hours) + ":" + str(self.minutes) + ":" + str(self.seconds)
        return time

    def tick(self):
        if self.is_zero() == True:
            return False

        if self.seconds.tick() == True:
            if self.minutes.tick() == True:
                self.hours.tick()

        return True

    def is_zero(self):
        if self.seconds == 0 and self.minutes == 0 and self.hours == 0:
            return True
        return False
