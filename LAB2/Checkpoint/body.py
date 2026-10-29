#Author: Roshan Shivnani
#Date: 10/29/2026
#Purpose/Description: make a body class for the solar system lab
#File: body.py
#Course: CS1

from cs1lib import *

#the body class initializes all 10 parameters called in earthmoon.py
class Body:
    def __init__(self, mass, x, y, v_x, v_y, radius, r, g, b):
        self.mass = mass
        self.x = x
        self.y = y
        self.v_x = v_x
        self.v_y = v_y
        self.radius = radius
        self.r = r
        self.g = g
        self.b = b

    #calculates the location planet should be drawn at given unit conversion then draws
    def draw(self, cx, cy, pixels_per_meter):
        draw_location_x = cx + (pixels_per_meter * self.x)
        draw_location_y = cy + (pixels_per_meter * self.y)

        set_fill_color(self.r, self.g, self.b)
        draw_circle(draw_location_x, draw_location_y, self.radius)

    #updates planet position by adding velocity
    def update_position(self, timestep):
        self.x = self.x + self.v_x * timestep
        self.y = self.y + self.v_y * timestep

    #updates planet velocity by adding acceleration
    def update_velocity(self, ax, ay, timestep):
        self.v_x = self.v_x + ax * timestep
        self.v_y = self.v_y + ay * timestep