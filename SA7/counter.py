#Author: Roshan Shivnani
#Date: 10/23/2026
#Purpose/Description: define a class counter that counts down
#File: counter.py
#Course: CS1

#creates a counter class
class Counter:

    #the constructor which auto run to make an instance of counter
    def __init__(self, limit, initial = 0, min_digits = 1):
        self.limit = limit
        self.min_digits = min_digits

        #checks if initial value valid if not give error and default at limit - 1
        if 0 <= initial <= limit - 1:
            self.value = initial
        else:
            print("error")
            self.value = limit - 1

    #returns counter value
    def get_value(self):
        return self.value

    #return value of counter as a string w/appropriate # of digits
    def __str__(self):
        string_value = str(self.value)

        #if value less then min digits then pad with zeros
        if len(string_value) < self.min_digits:
            #sees how many 0s needed to get to min digits then pads by that amount
            zero_number = self.min_digits - len(string_value)
            string_value = ('0' * zero_number) + string_value

        return string_value

    #each tick number decrease by one but if hit 0 loop back to start
    def tick(self):
        if self.value == 0:
            self.value = self.limit - 1
            return True
        else:
            self.value = self.value - 1
            return False
