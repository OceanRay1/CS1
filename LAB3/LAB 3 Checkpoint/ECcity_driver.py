#Author: Roshan Shivnani
#Date: 11/12/2026
#Purpose/Description: test city object by going through list of wrld cities and using it
#File: ECcity_driver.py
#Course: CS1

from ECcity import City
from cs1lib import *
from quicksort import *

#EC: global variable setup
setup_state = False
city_number = 0
chosen_sort_topic = "population"
city_object_list = []

#list of comparison functions with r
#uses return syntax specified in lab
def compare_alpha (city1, city2):
    #.lower for string comparison like lab example
    return city1.name.lower() <= city2.name.lower()

#compare 2 cities population (flip 2 and 1 since most to least populus)
def compare_population (city1, city2):
    return city2.population <= city1.population

#compare 2 cities latitude
def compare_latitude (city1, city2):
    return city1.latitude <= city2.latitude

def write_files():

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
def sort_algos():
    sort(city_object_list, compare_alpha)
    alpha_file = open("cities_alpha.txt", "w")
    for city in city_object_list:
        alpha_file.write(str(city) + "\n")
    alpha_file.close()

    #sort by population
    sort(city_object_list, compare_population)
    pop_file = open("cities_population.txt", "w")
    for city in city_object_list:
        pop_file.write(str(city) + "\n")
    pop_file.close()

    #sort by latitude
    sort(city_object_list, compare_latitude)
    lat_file = open("cities_latitude.txt", "w")
    for city in city_object_list:
        lat_file.write(str(city) + "\n")
    lat_file.close()

#EC: allows user to choose how and what on the map is displayed
def get_user_preferences():
    global city_number, chosen_criterion

    #EC: allow user to choose number of cities
    city_num = int(input("How many cities do you want to display (10-100)? : "))
    if city_num > 100:
        city_num = 100
    elif city_num < 10:
        city_num = 10
    city_number = city_num

    #EC: get which criteria to sort/view by
    print("Choose sorting criteria:")
    print("1: Alphabetical (Name)")
    print("2: Population (Most to least)")
    print("3: Latitude (South to north)")

    choice = input("Enter choice (1, 2, or 3): ").strip()

    #default option is population
    if choice == "1":
        sort(city_object_list, compare_alpha)
    elif choice == "3":
        sort(city_object_list, compare_latitude)
    else:
        sort(city_object_list, compare_population)

#parse csv file and display on the globe image
def world():
    global setup_state, city_number
    #EC: one time setup functions
    if setup_state == False:
        write_files()
        sort_algos()
        get_user_preferences()
        setup_state = True

    #map constants
    WIDTH = 720
    HEIGHT = 360
    center_x = WIDTH // 2
    center_y = HEIGHT // 2

    #EC: setup loading of different world image
    clear()
    img = load_image("ECglobe.jpg")
    draw_image(img, 0, 0)

    #EC: sort by different things
    for i in range(city_number):
        city_object_list[i].draw(center_x, center_y)

#EC: slower framerate so blinking can be seen
start_graphics(world, width=720, height=360, framerate=3)