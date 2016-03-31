'''
TO DO:

Add a score board and high scores
Add different modes (easy, medium, hard...)
Clean code (ie: make classes and functions to make it more moduler)
Create own assets
'''

import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

#set the display to be 800 x 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
#set the display caption
pygame.display.set_caption('A bit Racey')

black = (0,0,0)
white = (255,255,255)
#create a pygame clock to keep track of time
clock = pygame.time.Clock()
#used to see if the game is crashed

#set carImg to have the location of the race car image
carImg = pygame.image.load('racecar.png')
car_width = 73
car_height = 82

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

#used to place where the car is going to be
def car(x,y):
    gameDisplay.blit(carImg, (x,y))


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    
 #custom function to create messages on the screen   
def display_message(text_to_display):
	message_display(text_to_display)

def crash():
    message_display('You Crashed')
    game_loop()
		

def game_loop():
	
	gameExit = False
	x =  (display_width * 0.45)
	y = (display_height * 0.8)
	#used to change where the car is on the x axis. It's used inside the game loop as an updater.
	x_change = 0
	y_change = 0
	#Used to init the objects
	thing_startx = random.randrange(0, display_width)
	thing_starty = -600
	thing_speed = 13
	#set the object height and width
	thing_width = 100
	thing_height = 100

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			#Check to see if a key is pressed down
			if event.type == pygame.KEYDOWN:
				#If a ket is pressed down and it's the left arrow key set x_change to -5
				if event.key == pygame.K_LEFT:
					x_change = -9
				#if a key is pressed down and it's the right arrow ket set x_change to 5
				elif event.key == pygame.K_RIGHT:
					x_change = 9
					
				#Same as above but for the y axis instead	
				elif event.key ==pygame.K_UP:
					y_change = -9
				elif event.key == pygame.K_DOWN:
					y_change = 9
				
				#If the escape key is pressed close the game
				elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()
			#Check to see if a key is pressed up
			if event.type == pygame.KEYUP:
				#If a ket is pressed up and it's either the left arrow key or the right arrow key change x_change to 0
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
					x_change = 0
					y_change = 0
		#Update x with what ever x was and add the value of x_change to it
		x += x_change
		y += y_change
		
		#Set the object vairables with the ones used above (line 67 - 72)
		gameDisplay.fill(white)
		things(thing_startx, thing_starty, thing_width, thing_height, black)
		thing_starty += thing_speed
		car(x,y)
		
		
		#If x,  the x cord location of the car, is greater than the width of the screen minus the car width or if x is smaller than 0 then close the game.
		if x > display_width - car_width or x < 0:
			crash()
		if y > display_height - car_height or y < 0:
			crash()
			
			
		#When the object moves off the screen move it to a new position
		if thing_starty > display_height:
			thing_starty = 0 - thing_height
			thing_startx = random.randrange(0,display_width)
			print ("object respawned")
		#see if the y axis of the player object and the y axis of the obstical object cross over	
		if y < thing_starty + thing_height:
			print("y crossover occurred")
			
			#if it does then check to see if the x axis of both objects cross over
			if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x + car_width < thing_startx+thing_width:
				print("x crossover occurred")
				print("player crashed into object")
				crash()
				
		pygame.display.update()
		clock.tick(60)
		

#used to display the welcome message
gameDisplay.fill(white)
pygame.display.update()
display_message("Welcome!")
#Activate the game loop
game_loop()
#When the game loop ends close the game
pygame.quit()
#Quit python
quit()
