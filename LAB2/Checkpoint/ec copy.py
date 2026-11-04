#Author: Roshan Shivnani
#Date: 10/29/2026
#Purpose/Description: test the body/system class for the solar system lab
#File: system.py
#Course: CS1

from cs1lib import *
from system import System
from body import Body
from random import randint

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400

TIME_SCALE = 3.0e6        # real seconds per simulation second
PIXELS_PER_METER = 7 / 1e10  # distance scale for the simulation

FRAMERATE = 30              # frames per second
TIMESTEP = 1.0 / FRAMERATE  # time between drawing each frame

#starts planets at normal scale - can be changed with up/down keys
scale = 1
SCALE_UP_KEY = 'u'
SCALE_DOWN_KEY = 'd'

def main():
    set_clear_color(0, 0, 0)    # black background

    clear()

    #draw the system in its current state
    solar_system.draw(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2, PIXELS_PER_METER, scale)

    #update the system for its next state
    solar_system.update(TIMESTEP * TIME_SCALE)

    #EC: for education purposes actively display number of planets and scale factor
    set_stroke_color(1, 1, 1)
    #EC: for scale multiplies by 10 and gets int there so it rounded to one decimal then divide back by 10
    draw_text("Active scaling factor: " + str(int(scale * 10) / 10), 10, 25)
    draw_text("Number of bodies in orbit: " + str(len(solar_system.bodylist)), 10, 50)
    set_stroke_color(0, 0, 0)

#EC: allows the user to press u and d making planet bigger and smaller respectively
def key_press(key_press):
    global scale
    if key_press == SCALE_UP_KEY:
        #doesnt let planets grow bigger than 2x
        if scale < 2.0:
            scale += .1

    elif key_press == SCALE_DOWN_KEY:
        #doesnt let planets get smaller than .5x
        if scale > .51:
            scale -= .1

#EC: allows the user to add a planet into the system wherever they click on
def mouse_press(mx, my):
    center_x = WINDOW_WIDTH / 2
    center_y = WINDOW_HEIGHT / 2

    #gets relevant x,y for new planet via unit conversions
    meter_x = (mx - center_x) / (PIXELS_PER_METER)
    meter_y = (my - center_y) / (PIXELS_PER_METER)

    #adds a planet if the user's click isn't to close to the edge of the screen
    if WINDOW_WIDTH / 8 <= mx <= 7 * WINDOW_WIDTH / 8 and WINDOW_HEIGHT / 8 <= my <= 7 * WINDOW_HEIGHT / 8:
        #calc distance r from the Sun at 0,0
        r = (meter_x ** 2 + meter_y ** 2) ** 0.5

        if r > 0:
            #finds circular orbital speed w/formula v = square_root(G * M_sun / r)
            G = 6.67384e-11
            speed = (G * sun.mass  / r) ** 0.5

            #set velocity components vx & vy so it orbits instead of crashing/flying away
            vx = (meter_y / r) * speed
            vy = - (meter_x / r) * speed

            #EC: randomize color for new planet
            cr = randint(0, 255) / 255
            cg = randint(0, 255) / 255
            cb = randint(0, 255) / 255

            #planet added has set mass but the velocity corresponds w/position and color randomized
            new_planet = Body(5.9736e24, meter_x, meter_y, vx, vy, 6, cr, cg, cb)
            solar_system.bodylist.append(new_planet)

#All bodies & values from Prof. Campbell Canvas announcement
# added jupiter and -778.5 reduced to -678.9 for fun
# from https://nssdc.gsfc.nasa.gov/planetary/factsheet/
sun = Body(1.98892e30, 0, 0, 0, 0, 15, 1, 1, 0)  # yellow sun
mercury = Body(0.33e24, -57.9e9, 0, 0, 47890, 4, 1, 0.5, 0)  # orange mercury
venus = Body(4.87e24, -108.2e9, 0, 0, 35040, 6, 0, 1, 0)  # green venus
earth = Body(5.9736e24, -149.6e9, 0, 0, 29790, 6, 0, 0, 1)  # blue earth
mars = Body(0.642e24, -227.9e9, 0, 0, 24140, 6, 1, 0, 0)  # red mars
jupiter = Body(1898e24, -678.9e9, 0, 0, 13100, 8, 1, 0, 1)  # pink jupiter
solar_system = System([sun, mercury, venus, earth, mars, jupiter])

start_graphics(main, 2400, framerate=FRAMERATE, key_press=key_press, mouse_press=mouse_press)
