#Author: Roshan Shivnani
#Date: 11/12/2026
#Purpose/Description: test city object by going through list of wrld cities and using it
#File: city_driver.py
#Course: CS1

from city import City
from cs1lib import *

#test for parsing csv file and displaying on world image
def world():

    #the list of cities as objects not strings
    city_object_list = []

    #map constants
    WIDTH = 720
    HEIGHT = 360
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    #setup loading of world image
    clear()
    img = load_image("world.png")
    draw_image(img, 0, 0)

    #read from the world_cities.txt file and write the final output to out files
    in_file = open("world_cities.txt", "r")
    out_file = open("cities_out.txt", "w")

    #loop through each city in world city
    for line in in_file:
        #split by commas
        edit_line = line.strip().split(",")

        #each part of city ex: name or region read as parameter to create a city object
        new_city = City(edit_line[0], edit_line[1], edit_line[2], edit_line[3], edit_line[4], edit_line[5])

        #append new city object to city list
        city_object_list.append(new_city)

        #city object for each city written to output file
        out_file.write(str(new_city))
        out_file.write("\n")

    #drawing first 10 cities at first to test
    for i in range(10):
        city_object_list[i].draw(center_x, center_y)

    #close both files
    in_file.close()


start_graphics(world, width=720, height=360)