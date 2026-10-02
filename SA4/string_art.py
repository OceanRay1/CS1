# Author: Roshan Shivnani
# Date: 09/29/2026
# Purpose/Description: Draw String Art
# File: stringart.py
# Course: CS1

from cs1lib import *

#Size of square side & width/height of output window size
WIN_SIZE = 400
x = 0
y = WIN_SIZE
setup = False

def string_art():
    #Makes x & y global var so they can be used for animation
    global x, y, setup

    #Clears the canvas one time at start of animation
    if not setup:
        clear()
        setup = True

    #Setup drawing variables
    OFFSET = 20
    set_stroke_width(3)
    set_stroke_color(0, .75, 1)

    #Sticks two "thumbtacks" (points) 
    draw_point(x, y)
    draw_point(y, WIN_SIZE - x)

    #Draws a line between them in color blue & smaller size so visible
    set_stroke_width(2)
    set_stroke_color(0, .75, 1)
    draw_line(x, y, y, WIN_SIZE - x)

    #To ensure drawing works on each side of window, if statement w/corresponding x & y used current side of square
    #The offset adjusts point in the either x or y-axis given which side of square the function is currently on
    if y > 0 and x == 0:
        y -= OFFSET

    elif x < WIN_SIZE and y == 0:
        x += OFFSET

    elif y < WIN_SIZE:
        y += OFFSET

    elif x > 0:
        x -= OFFSET

start_graphics(string_art, width = WIN_SIZE, height = WIN_SIZE)
