#!/usr/bin/python3

# Imports
from sense_hat import SenseHat
import random
import socket
import time
import encodings
from time import sleep

# Variables
sense = SenseHat()
brown = (181,101,29)
white = (255,255,255)
grey = (64,64,64)
green = (82,235,5)
red = (255,0,0)
glove_y = 3
glove_x = 3

# Draw Fence
def draw_fence():
	for x in range(8):
		sense.set_pixel(x, 0, grey)
	for y in range(8):
		sense.set_pixel(0, y, grey)
	for x in range(1,8):
		sense.set_pixel(x, 1, green)
		sense.set_pixel(x, 2, green)
		sense.set_pixel(x, 3, green)
		sense.set_pixel(x, 4, green)
		sense.set_pixel(x, 5, green)
		sense.set_pixel(x, 6, green)
		sense.set_pixel(x, 7, green)




# Draw the glove
def draw_glove():
	sense.clear(0,0,0)
	draw_fence()
	global glove_x
	global glove_y
	sense.set_pixel(glove_x, glove_y, brown)
	sense.set_pixel(glove_x, glove_y + 1, brown)
	sense.set_pixel(glove_x + 1, glove_y + 1, brown)
	sense.set_pixel(glove_x + 1, glove_y, brown)



# Initial glove draw
draw_glove()

# Movements
def move_left(event):
	global glove_x
	if event.action == 'pressed' and glove_x > 1:
		glove_x -= 1
		draw_glove()

def move_right(event):
	global glove_x
	if event.action == 'pressed' and glove_x < 6:
		glove_x += 1
		draw_glove()

def move_down(event):
	global glove_y
	if event.action == 'pressed' and glove_y < 6:
		glove_y += 1
		draw_glove()

def move_up(event):
	global glove_y
	if event.action == 'pressed' and glove_y > 1:
		glove_y -= 1
		draw_glove()

# Pitch ball
def middle_click(event):
	if event.action == 'pressed':
		connect()

def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('10.41.10.38', 43594)) #tims IP 10.41.10.38

	X = s.recv(1024)
	sleep(0.50)
	Y = s.recv(1024)
	Xaxis = X.decode('utf8')
	Yaxis = Y.decode('utf8')
	global numX
	global numY
	numX = int(Xaxis)
	numY = int(Yaxis)
	draw_ball()

# Function for taking input coordinates
def draw_ball():
	global numX
	global numY
	sense.set_pixel(numX, numY, white)
	sleep(4.0)
	check_position()

def check_position():
	global numX
	global numY
	global glove_x
	global glove_y
	if numY == glove_y and numX == glove_x:
		sense.show_message('You Win!', 0.075, text_colour=green)
	elif numY == glove_y + 1 and numX == glove_x + 1:
		sense.show_message('You Win!', 0.075, text_colour=green)
	elif numY == glove_y + 1 and numX == glove_x:
		sense.show_message('You Win!', 0.075, text_colour=green)
	elif numY -- glove_y and numX == glove_x + 1:
		sense.show_message('You Win!', 0.075, text_colour=green)
	else:
		sense.show_message('Game Over, You Lose', 0.075, text_colour=red)



sense.stick.direction_left = move_left
sense.stick.direction_right = move_right
sense.stick.direction_down = move_down
sense.stick.direction_up = move_up
sense.stick.direction_middle = middle_click

while True:
	sleep(0.25)
