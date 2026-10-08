#Author: Roshan Shivnani
#Date: 10/8/2026
#Purpose/Description: Make a playable version of pong
#File: pong.py
#Course: CS1

from cs1lib import *

#Window display info
width = 400
height = 400
setupstate = False

#Paddle setup (p1 = paddle 1, p2 = paddle 2)
p1y1 = 0
p2y1 = 320
paddle_height = 80
paddle_width = 20
paddle_speed = 10

#Movement keys
p1keyup = 'a'
p1keydown = 'z'
p2keyup = 'k'
p2keydown = 'm'

#Boolean expressions that track if paddle should be moving
p1up = False
p1down = False
p2up = False
p2down = False

#Function containing one time commands to setup background
def setup():
    global setupstate

    #Uses Dartmouth green for background & paddle color :)
    set_clear_color(0, 105/256, 62/256)
    set_fill_color(0, 1, 0)
    set_stroke_width(2)
    enable_fill()
    setupstate = True

#Allows users to press keys that control the paddle's position
def key_pressed(key):
    global p1up, p2up, p1down, p2down, speed
    if key == p1keyup:
        p1up = True
    if key == p1keydown:
        p1down = True
    if key == p2keyup:
        p2up = True
    if key == p2keydown:
        p2down = True

def key_released(key):
    global p1up, p2up, p1down, p2down, speed
    if key == p1keyup:
        p1up = False
    if key == p1keydown:
        p1down = False
    if key == p2keyup:
        p2up = False
    if key == p2keydown:
        p2down = False

def update_positions():
    global p1y1, p2y1, p1up, p2up, p1down, p2down, speed
    if p1up == True:
        p1y1 = p1y1 + paddle_speed
    if p1down == True:
        p1y1 = p1y1 - paddle_speed
    if p2up == True:
        p2y1 = p2y1 + paddle_speed
    if p2down == True:
        p2y1 = p2y1 - paddle_speed

    if p1y1 < 0:
        p1y1 = 0
    elif p1y1 > 320:
        p1y1 = 320
    if p2y1 < 0:
        p2y1 = 0
    elif p2y1 > 320:
        p2y1 = 320

def pong():
    clear()
    #One-time execute of setup commands
    if not setupstate:
        setup()

    #Constantly updates paddles' positions
    update_positions()

    draw_rectangle(0, p1y1, paddle_width, paddle_height)
    draw_rectangle(380, p2y1, paddle_width, paddle_height)

#Pong with event handlers
start_graphics(pong, width=width, height=height,
               key_press=key_pressed, key_release=key_released)