# Author: Roshan Shivnani
# Date: 10/1/2026
# Purpose/Description: Make a custom chalkboard
# File: chalkboard.py
# Course: CS1

from cs1lib import *

#Initial global variables
old_x = 200
old_y = 200
current_x = 200
current_y = 200
setupstate = False

#Switches color to corresponding key pressed
def color_check():
    if is_key_pressed("w"):
        set_stroke_color(1, 1, 1)
    elif is_key_pressed("r"):
        set_stroke_color(1, 0, 0)
    elif is_key_pressed("g"):
        set_stroke_color(0, 1, 0)
    elif is_key_pressed("b"):
        set_stroke_color(0, 0, 1)
    elif is_key_pressed("y"):
        set_stroke_color(1, 1, 0)

#Function containing one time commands to setup background
def setup():
    global setupstate
    set_clear_color(0, 0, 0)
    clear()
    set_stroke_color(1, 1, 1)
    setupstate = True

#Function that allows user to draw a line via keeping track of the cursor's position
def draw():
    global old_x, old_y, current_x, current_y
    current_x = mouse_x()
    current_y = mouse_y()
    
    #draws line between where cursor just was and currently is
    if is_mouse_pressed():
        draw_line(old_x, old_y, current_x, current_y)

    old_x = current_x
    old_y = current_y

def chalkboard():
    #One-time execute of setup commands
    if not setupstate:
        setup()

    #Constantly checks and adjusts mouse (position & color)
    color_check()
    draw()

start_graphics(chalkboard)