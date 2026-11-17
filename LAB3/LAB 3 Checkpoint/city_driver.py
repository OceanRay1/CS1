#Author: Roshan Shivnani
#Date: 11/12/2026
#Purpose/Description: test city object by going through list of wrld cities and using it
#File: city_driver.py
#Course: CS1

from city import City
from cs1lib import *

#list of comparison functions with r
#uses return syntax specified in lab
def comp_alpha (city1, city2):
    #.lower for string comparison like lab example
    return city1.name.lower() <= city2.name.lower()

#compare 2 cities population (flip 2 and 1 since most to least populus)
def comp_pop (city1, city2):
    return city2.population <= city1.population

#compare 2 cities latitude
def comp_lat (city1, city2):
    return city1.latitude <= city2.latitude


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
        line = line.strip()
        edit_line = line.split(",")

        #each part of city ex: name or region read as parameter to create a city object
        new_city = City(edit_line[0], edit_line[1], edit_line[2], edit_line[3], edit_line[4], edit_line[5])

        #append new city object to city list
        city_object_list.append(new_city)

        #city object for each city written to output file
        out_file.write(str(new_city))
        out_file.write("\n")

    #close both files
    in_file.close()
    out_file.close()

    #sorting algorithms
    #sort by alphabetically
    sort(city_object_list, comp_alpha)
    alpha_file = open("cities_alpha.txt", "w")
    for city in city_object_list:
        alpha_file.write(str(city) + "\n")
    alpha_file.close()

    #sort by population
    sort(city_object_list, comp_pop)
    pop_file = open("cities_population.txt", "w")
    for city in city_object_list:
        pop_file.write(str(city) + "\n")
    pop_file.close()

    #sort by latitude
    sort(city_object_list, comp_lat)
    lat_file = open("cities_latitude.txt", "w")
    for city in city_object_list:
        lat_file.write(str(city) + "\n")
    lat_file.close()

    #sort again by population
    sort(city_object_list, comp_pop)

    #drawing first 10 cities at first to test
    for i in range(25):
        city_object_list[i].draw(center_x, center_y)

start_graphics(world, width=720, height=360)
