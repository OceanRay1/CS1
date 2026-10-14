#Author: Roshan Shivnani
#Date: 10/11/2026
#Purpose/Description: Make a playable version of pong
#File: FINALpong.py
#Course: CS1

from cs1lib import *

#Window display info
WIDTH = 400
HEIGHT = 400
setupstate = True

#Paddle setup (p1 = paddle 1, p2 = paddle 2)
PADDLE_HEIGHT = 80
PADDLE_WIDTH = 20
PADDLE_SPEED = 10
p1y1 = 0
p2y1 = HEIGHT - PADDLE_HEIGHT

#Movement keys
P1KEYUP = 'a'
P1KEYDOWN = 'z'
P2KEYUP = 'k'
P2KEYDOWN = 'm'

#Boolean expressions that track if paddle should be moving
p1up = False
p1down = False
p2up = False
p2down = False

#Setting up Ping Pong Ball
ball_x = WIDTH / 2
ball_y = HEIGHT / 2
ball_vx = 0
ball_vy = 0
BALL_RADIUS = 10

#Game State info
gamestate = False
QUITKEY = 'q'
RESET_GAMESTATEKEY = ' '

#Allows users to press keys that control the paddle's position
def key_pressed(key):
    global p1up, p2up, p1down, p2down, gamestate, ball_vx, ball_vy

    #Movement keys
    if key == P1KEYUP:
        p1up = True
    if key == P1KEYDOWN:
        p1down = True
    if key == P2KEYUP:
        p2up = True
    if key == P2KEYDOWN:
        p2down = True

    #Allows user to start the game if the game is over
    if key == RESET_GAMESTATEKEY and gamestate == False:
        reset_gamestate()
        ball_vx = -5
        ball_vy = -5
        gamestate = True

    #User can quit game at any point
    if key == QUITKEY:
        cs1_quit()

#Stops paddle movement when the user releases key
def key_released(key):
    global p1up, p2up, p1down, p2down

    #Movement keys
    if key == P1KEYUP:
        p1up = False
    if key == P1KEYDOWN:
        p1down = False
    if key == P2KEYUP:
        p2up = False
    if key == P2KEYDOWN:
        p2down = False

#Moves the paddle w/respect to the key that was pressed
def paddle_positions():
    global p1y1, p2y1
    if p1up == True:
        p1y1 = p1y1 - PADDLE_SPEED
    if p1down == True:
        p1y1 = p1y1 + PADDLE_SPEED
    if p2up == True:
        p2y1 = p2y1 - PADDLE_SPEED
    if p2down == True:
        p2y1 = p2y1 + PADDLE_SPEED

    #Stops paddle from moving outside window via boundaries at top/bottom
    if p1y1 < 0:
        p1y1 = 0
    elif p1y1 > HEIGHT - PADDLE_HEIGHT:
        p1y1 = HEIGHT - PADDLE_HEIGHT
    if p2y1 < 0:
        p2y1 = 0
    elif p2y1 > HEIGHT - PADDLE_HEIGHT:
        p2y1 = HEIGHT - PADDLE_HEIGHT

#The function that resets game to default (ball pos, velocity, etc)
def reset_gamestate():
    global p1y1, p2y1, ball_x, ball_y, ball_vx, ball_vy, gamestate
    gamestate = False

    #paddle & ball starting positions/velocity
    p1y1 = 0
    p2y1 = HEIGHT - PADDLE_HEIGHT
    ball_x = WIDTH / 2
    ball_y = HEIGHT / 2
    ball_vx = 0
    ball_vy = 0

#Updates ball movement & checks the ball's position/collision
def ball_movement():
    global ball_x, ball_y, ball_vx, ball_vy, gamestate

    #Any ball movement can only happen when the game is running
    if gamestate == True:
        ball_x = ball_x + ball_vx
        ball_y = ball_y + ball_vy

        #Checks for ball collision w/top or bottom of board (resets ball to edge if so)
        if ball_y <= 0:
            ball_vy = -ball_vy
            ball_y = 0
        if ball_y >= HEIGHT:
            ball_vy = -ball_vy
            ball_y = HEIGHT

        #Checks for ball collision w/either paddle which reverse the balls momentum
        if ball_x <= PADDLE_WIDTH and ball_y >= p1y1 and ball_y <= p1y1 + PADDLE_HEIGHT:
            ball_vx = -ball_vx
        if ball_x >= WIDTH - PADDLE_WIDTH and ball_y >= p2y1 and ball_y <= p2y1 + PADDLE_HEIGHT:
            ball_vx = -ball_vx

        #Check if ball hits either end of window and ends game if so
        if ball_x <= 0 or ball_x >= WIDTH:
            reset_gamestate()

#Constantly draws the paddles & ball at correct position
def draw():
    #Paddle drawing
    draw_rectangle(0, p1y1, PADDLE_WIDTH, PADDLE_HEIGHT)
    draw_rectangle(WIDTH - PADDLE_WIDTH, p2y1, PADDLE_WIDTH, PADDLE_HEIGHT)

    #Ball drawing
    draw_circle(ball_x, ball_y, BALL_RADIUS)

def pong():
    clear()

    #Uses Dartmouth green for background & paddle color :)
    set_clear_color(0, 105 / 255, 62 / 255)
    set_fill_color(0, 1, 0)
    set_stroke_width(2)

    #Constantly updates paddles' positions
    paddle_positions()

    #Constantly draws & updates the paddles' and ball's correct position
    draw()
    ball_movement()

#Pong w/event handlers
start_graphics(pong, width=WIDTH, height=HEIGHT,
               key_press=key_pressed, key_release=key_released)