#Author: Roshan Shivnani
#Date: 11/12/2026
#Purpose/Description: setup a reusable city class
#File: city.py
#Course: CS1

from cs1lib import *

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

    #print the 4 specified parameters with commas and no spaces as assignment specified
    def __str__(self):
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," + str(self.longitude)

    #takes coords and draws on world map
    def draw(self, center_x, center_y):
        #adjust by lat/long away from the center to see where to draw circle
        #px and py are scaled values to match map
        px = center_x + self.longitude * 2
        py = center_y - self.latitude * 2
        set_fill_color(1, 0,0)
        draw_circle(px, py, 5)


