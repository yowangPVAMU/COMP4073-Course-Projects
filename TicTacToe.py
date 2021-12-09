#Libraries
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_RELEASED
import time
#import tkinter
#from tkinter import *
sense = SenseHat()

#Initial position of cursor
x=3
y=3

#Number of columns of LEDs
col = 8

#Team 1 (red) will go first
team1 = 255
team2 = 0

#Selectcolor is used to slightly change the color of the cursor before selecting a square
selectcolor = 150

#Make TicTacToe board on LED display
a = [100,100,100]   #White
b = [0,0,0]         #Turned off
rd = [255, 0, 0]    #Red
bl = [0, 0, 255]    #Blue

#These values will change:
board = [
    b, b, a, b, b, a, b, b,
    b, b, a, b, b, a, b, b,
    a, a, a, a, a, a, a, a,
    b, b, a, b, b, a, b, b,
    b, b, a, b, b, a, b, b,
    a, a, a, a, a, a, a, a,
    b, b, a, b, b, a, b, b,
    b, b, a, b, b, a, b, b,
    ]
#These values will never change:
boardreset = [
    b, b, a, b, b, a, b, b,
    b, b, a, b, b, a, b, b,
    a, a, a, a, a, a, a, a,
    b, b, a, b, b, a, b, b,
    b, b, a, b, b, a, b, b,
    a, a, a, a, a, a, a, a,
    b, b, a, b, b, a, b, b,
    b, b, a, b, b, a, b, b,
    ]


#Turn on the TicTacToe board and cursor
sense.set_pixels(board)
sense.set_pixel(x,y,team1,selectcolor,team2)

#Run this function any time the joystick is pushed in        
def select(event):
    global team1, team2
    global x, y
    global board

    #If the joystick is pressed and this spot on the board has not already been selected:
    if event.action == ACTION_PRESSED and board[(col*y)+x] == b:

        if team1==255:      #If it is the red player's turn:
            #Set the four LEDs to red
            board[(col*y)+x] = rd
            board[(col*(y+1))+x] = rd
            board[(col*y)+(x+1)] = rd
            board[(col*(y+1))+(x+1)] = rd
            #Switch to blue players turn:
            team1 = 0
            team2 = 255
        else:               #If it is the blue player's turn:
            #Set the four LEDs to blue
            board[(col*y)+x] = bl
            board[(col*(y+1))+x] = bl
            board[(col*y)+(x+1)] = bl
            board[(col*(y+1))+(x+1)] = bl
            #Switch to red player's turn:
            team1 = 255
            team2 = 0

        #Refresh the board to display the newly selected square:
        sense.set_pixels(board)

        #If all the spaces on the board are filled up, blink the board twice and refresh:
        if (board[0] !=b and board[3] !=b and board[6] !=b and board[24] !=b and board[27] !=b and board[30] !=b and board[48] !=b and board[51] !=b and board[54] !=b):
            time.sleep(2)
            sense.set_pixels(boardreset)
            time.sleep(1)
            sense.set_pixels(board)
            time.sleep(1)
            sense.set_pixels(boardreset)
            time.sleep(1)
            sense.set_pixels(board)
            time.sleep(1)
            board = [
                b, b, a, b, b, a, b, b,
                b, b, a, b, b, a, b, b,
                a, a, a, a, a, a, a, a,
                b, b, a, b, b, a, b, b,
                b, b, a, b, b, a, b, b,
                a, a, a, a, a, a, a, a,
                b, b, a, b, b, a, b, b,
                b, b, a, b, b, a, b, b,
                ]
            sense.set_pixels(board)
        #Reset the cursor:     
        x=3
        y=3
        sense.set_pixel(x,y,team1,selectcolor,team2)

        
#Run this function any time the joystick is pushed up
def pushed_up(event):
    global y, board
    if event.action != ACTION_RELEASED:
        #Remove the cursor:
        sense.set_pixels(board)
        #Change the position of the cursor:
        y = y-3
        if y<0:
            y=0
        #Display the cursor in its new position:
        sense.set_pixel(x,y,team1,selectcolor,team2)


#Run this function any time the joystick is pushed down
def pushed_down(event):
    global y, board
    if event.action != ACTION_RELEASED:
        sense.set_pixels(board)
        y = y+3
        if y>6:
            y=6
        sense.set_pixel(x,y,team1,selectcolor,team2)

#Run this function any time the joystick is pushed left
def pushed_left(event):
    global x, board
    if event.action != ACTION_RELEASED:
        sense.set_pixels(board)
        x = x-3
        if x<0:
            x=0
        sense.set_pixel(x,y,team1,selectcolor,team2)

#Run this function any time the joystick is pushed right
def pushed_right(event):
    global x, board
    if event.action != ACTION_RELEASED:
        sense.set_pixels(board)
        x = x+3
        if x>6:
            x=6
        sense.set_pixel(x,y,team1,selectcolor,team2)


if __name__ == '__main__':
    try:
        while True:
            #Sense for joystick movements and run the designated function
            sense.stick.direction_up = pushed_up  
            sense.stick.direction_down = pushed_down  
            sense.stick.direction_left = pushed_left  
            sense.stick.direction_right = pushed_right
            sense.stick.direction_middle = select

    # Turn off by pressing CTRL + C
    except KeyboardInterrupt:
        print("Game stopped by User")
        sense.clear()



