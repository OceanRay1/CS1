# Author: Roshan Shivnani
# Date: 09/22/2026
# Purpose/Description: Drawing Book Cover (One fish, Two fish, Red fish, Blue fish) with cs1lib
# File: drawing.py
# Course: CS1

from SA2.cs1lib import *

#configures general text/line settings
def text_settings():
    set_font("Arial")
    set_font_bold()
    set_font_italic()
    set_font_size(40)
    set_stroke_width(20)

def make_background_yellow():
    set_clear_color(1, 1, 0)
    clear()

def set_fill_white():
    set_fill_color(1, 1, 1)

def set_fill_green():
    set_fill_color(0, 1, 0)

def set_fill_red():
    set_fill_color(1, 0, 0)

def set_fill_blue():
    set_fill_color(0, 0, 1)

def set_fill_cyan():
    set_fill_color(0, 1, 1)

#draws a fish with eye/tail at a given position (x, y)
def draw_fish(x, y):
    draw_circle(x, y, 50)
    draw_triangle(x + 50, y, x + 120, y + 50, x + 120, y - 50)
    set_fill_color(0, 0, 0)
    draw_circle(x - 25, y - 25, 5)

def draw_OneFishTwoFish():
    #Background/Book color & text formatting set
    make_background_yellow()
    text_settings()
    set_fill_cyan()
    draw_rectangle(50, 20, 700, 660)

    #adds book cover
    set_fill_white()
    draw_fish(200, 100)
    draw_text("One fish", 450, 115)
    set_fill_green()
    draw_fish(200, 250)
    draw_text("Two fish", 450, 265)
    set_fill_red()
    draw_fish(200, 400)
    draw_text("Red fish", 450, 415)
    set_fill_blue()
    draw_fish(200, 550)
    draw_text("Blue fish", 450, 565)
    draw_text("By Roshan Shivnani: Storytime!", 100, 650)

    #cover outline
    draw_line(50, 680, 750, 680)
    draw_line(50, 20, 50, 680)
    draw_line(50, 20, 750, 20)
    draw_line(750, 20, 750, 680)

start_graphics(draw_OneFishTwoFish, width = 800, height = 700)