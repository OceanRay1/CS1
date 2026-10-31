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
        self.bodylist = bodylist

    def compute_acceleration(self, n):
            #gravitational constant
            G =  6.67384 * 10 ** -11

            #sums up total x & y acceleration components starting from 0
            a_x_total = 0
            a_y_total = 0

            #checks how each planet in system besides itself effects a_x & a_y
            for i in range(len(self.bodylist)):

                #skips over the planet itself so calculation not messed up
                if i != n:

                    #calculates distance apart in x and y coords
                    dx = self.bodylist[i].x - self.bodylist[n].x
                    dy = self.bodylist[i].y - self.bodylist[n].y

                    #radius used to calculate total acceleration, then split into x and y component
                    #calculations used from lab's canvas assignment
                    r = ((dx ** 2) + (dy ** 2)) ** (1/2)
                    a = G * self.bodylist[i].mass / (r * r)
                    a_x_total += a * (self.bodylist[i].x - self.bodylist[n].x) / r
                    a_y_total += a * (self.bodylist[i].y - self.bodylist[n].y) / r

            #returned as tuple data structure
            return a_x_total, a_y_total

    #draws the position of each planet in the system
    def draw(self, cx, cy, pixels_per_meter):
        for body in self.bodylist:
            body.draw(cx, cy, pixels_per_meter)

    #updates the position of each planet given a certain acceleration
    def update(self, timestep):

        #creates a list for each plane number and stores its x & y acceleration
        acceleration_list = []
        for i in range(len(self.bodylist)):
            acceleration_list.append(self.compute_acceleration(i))

        for i in range(len(self.bodylist)):
            #gets the x and y acceleration from list to use in velocity update calc
            ax, ay = acceleration_list[i]

            #calculate & update acceleration values in x/y direction
            self.bodylist[i].update_velocity(ax, ay, timestep)
            self.bodylist[i].update_position(timestep)
