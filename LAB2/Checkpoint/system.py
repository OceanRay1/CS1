#Author: Roshan Shivnani
#Date: 10/29/2026
#Purpose/Description: make a system class for the solar system lab
#File: system.py
#Course: CS1

from cs1lib import *
from body import Body

#creates a System class with multiple planets ex: like the Solar System
class System:

    #takes the list of planets and initializes each one
    def __init__(self, bodylist):
        for i in range(len(bodylist)):
            self.bodylist = bodylist

    #draws the position of each planet in the system
    def draw(self, cx, cy, pixels_per_meter):
        for body in self.bodylist:
            body.draw(cx, cy, pixels_per_meter)

    #updates the position of each planet given a certain acceleration
    def update(self, timestep):
        for body in self.bodylist:
            body.update_position(timestep)
            body.update_velocity(timestep, 0.005, 0)