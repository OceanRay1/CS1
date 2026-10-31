#Author: Roshan Shivnani
#Date: 10/29/2026
#Purpose/Description: test the body/system class for the solar system lab
#File: earthmoon.py
#Course: CS1

from cs1lib import *
from system import System
from body import Body

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 100000         # real seconds per simulation second
PIXELS_PER_METER = 3 / 1e7  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

def main():

    set_clear_color(0, 0, 0)    # black background

    clear()

    # Draw the system in its current state.
    earth_moon.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER)

    # Update the system for its next state.
    earth_moon.update(TIMESTEP * TIME_SCALE)


##All bodies & values from Prof. Campbell Canvas announcement
# added jupiter and -778.5 reduced to -678.9 for fun
# from https://nssdc.gsfc.nasa.gov/planetary/factsheet/
sun = Body(1.98892e30, 0, 0, 0, 0, 15, 1, 1, 0)  # yellow sun
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 4, 1, 0.5, 0)  # orange mercury
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 6, 0, 1, 0)  # green venus
earth = Body(5.9736e24, -149.6e9, 0, 0, 29790, 6, 0, 0, 1)  # blue earth
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 6, 1, 0, 0)  # red mars
jupiter = Body(1898e24, -678.9e9, 0, 0, 13100, 8, 1, 0, 1)  # pink jupiter
earth_moon = System([sun, mercury, venus, earth, mars, jupiter])

start_graphics(main, 2400, framerate=FRAMERATE)
