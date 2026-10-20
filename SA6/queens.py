#Author: Roshan Shivnani
#Date: 10/19/2023
#Purpose: N-queens validation problem solution

from cs1lib import *
from random import randint

WIN_SIZE = 500
N = 5
CELL_SIZE = WIN_SIZE // N
first = True
end = False
board_lol = []

#Create NxN board with empty cells (all cells are false)
def initialize_empty_board():
    i = 0
    while i < N:
        board_lol.append([])
        j = 0
        while j < N:
            board_lol[i].append(False)
            j = j + 1

        i = i + 1


#Capture mouse location and find the cell and flip
#the true-false flag

def my_mpress(mx, my):
    col = mx // CELL_SIZE
    row = my // CELL_SIZE

    board_lol[row][col] = not board_lol[row][col]

# The function that takes a list of lists
# representation of the board
# and draw the chessboard. It draws placed
# queens as red circles.

def draw_board(glol, n):
    # clear background
    set_clear_color(1, 1, 1)
    clear()

    if len(glol) != n:
        print("Wrong outer list length", n)
        return
    sqr_width = WIN_SIZE // n
    i = 0
    while i < n:
        if len(glol[i]) != n:
            print("Wrong inner list length")
            return
        j = 0
        while j < n:
            if (j+i) % 2 == 0:
                set_fill_color(1, 1, 1)
            else:
                set_fill_color(0.5, 0.5, 0.5)

            sqr_x = i * sqr_width
            sqr_y = j * sqr_width
            draw_rectangle(sqr_y, sqr_x, sqr_width, sqr_width)

            #Check if that cell has a queen and draw a
            #circle in red.
            if glol[i][j] == True:
                set_fill_color(0.9, 0, 0)
                draw_circle(sqr_y+sqr_width//2, sqr_x+sqr_width//2, sqr_width//10)

            j = j +1
        i = i + 1

# This function takes a list of lists representing
# the N*N chessboard with N queens placed randomly on
# board and returns True if no two queens
# attach each other. Otherwise, it returns False.

def check_vertical_lines(glol, i, j):
    #For the specified row if more than 2 queens in a row true returned
    count = 0
    for column in range(len(glol)):
        if glol[column][j] == True:
            count = count + 1
        if count > 1:
            return True
    return False

def check_horizontal_lines(glol, i, j):
    #For the specified column if more than 2 queens in a row true returned
    count = 0
    for row in range(len(glol)):
        if glol[i][row] == True:
            count = count + 1
        if count > 1:
            return True
    return False

def check_diagonal_left(glol, i, j):
    #Continues moving up and to the left to see if something is diagonally to the left
    # Does until at top right corner so it don't try to get index out of board
    while i > 0 and j > 0:
        #move up
        i = i - 1
        #to the right
        j = j - 1
        if glol[i][j] == True:
            return True
    return False

def check_diagonal_right(glol, i, j):
    #Continues moving up and to the right to see if something is diagonally to the right
    #Does until at top right corner so it don't try to get index out of board
    while i > 0 and j < N - 1:
        #move up
        i = i - 1
        #to the right
        j = j + 1
        if glol[i][j] == True:
            return True
    return False

def check_board(glol):
    #By looping through row & column every square is checked
    #i is the index of row & j is the index of the column
    for i in range(len(glol)):
        for j in range(len(glol)):

            #For every queen each square they reach is checked and if queen there too false is returned
            if glol[i][j] == True:
                if check_diagonal_left(glol, i, j) == True:
                    return False
                if check_diagonal_right(glol, i, j) == True:
                    return False
                if check_vertical_lines(glol, i, j) == True:
                    return False
                if check_horizontal_lines(glol, i, j) == True:
                    return False

    #If no queens see each other than game still runs
    return True

#Main draw function
def my_draw():
    global first, end
    if first:
        set_clear_color(1, 1, 1)
        clear()
        first = False

    check = check_board(board_lol)
    end = not check #end is true when check_board returns False

    draw_board(board_lol, N)
    if end:
        # clear()
        # set_clear_color(1, 1, 1)
        draw_board(board_lol, N)
        set_font_size(50)
        draw_text("The End", 150, 250)


initialize_empty_board()
start_graphics(my_draw, width=WIN_SIZE, height=WIN_SIZE, mouse_press=my_mpress)