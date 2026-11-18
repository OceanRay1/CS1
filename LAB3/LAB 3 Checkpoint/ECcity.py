#Author: Roshan Shivnani
#Date: 11/12/2026
#Purpose/Description: setup a reusable city class
#File: ECcity.py
#Course: CS1

from cs1lib import *
from random import randint

#creates a reusable city class
class City():

    #initialize the city class w/the 6 specified parameters
    def __init__(self, code, name, region, population, latitude, longitude):
        self.code = code
        self.name = name
        self.region = region
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)
        #EC each point gets randomized rgb color - and capped at 220 so not to close to white (1,1,1)
        self.rand_red = randint(0, 220) / 256
        self.rand_green = randint(0, 220) / 256
        self.rand_blue = randint(0, 220) / 256
        self.blink = True

    #print the 4 specified parameters with commas and no spaces as assignment specified
    def __str__(self):
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)

    #takes coords and draws on world map
    def draw(self, center_x, center_y):
        #adjust by lat/long away from the center to see where to draw circle
        #px and py are scaled values to match map
        px = center_x + self.longitude * 2
        py = center_y - self.latitude * 2

        #EC randomize the color of each city updating each frame
        if self.blink == True:
            set_fill_color(self.rand_red, self.rand_green, self.rand_blue)
            self.blink = False
        else:
            set_fill_color(1, 1, 1)
            self.blink = True

        draw_circle(px, py, 5)

        #EC write name for each name on the map
        set_font_bold()
        set_font_size(10)
        draw_text(self.name, px - 15, py - 7.5)


