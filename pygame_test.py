import pygame
import time
import random
import entity
import text_handler

pygame.init()

display_width = 1000
display_height = 900

#set the display to be 800 x 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
#set the display caption
pygame.display.set_caption('Dodge shit get hit')

text_handler = text_handler.textHandler(display_width,display_height, gameDisplay)
race_car = entity.player(pygame.image.load('racecar.png'), 73, 82 ,display_width*0.45, display_height*0.8)
obstacle = entity.squareObject(pygame.image.load('square.png'),114,106,30,50)
black = (0,0,0)
white = (255,255,255)
#create a pygame clock to keep track of time
clock = pygame.time.Clock()

 #custom function to create messages on the screen   
def display_message(text_to_display):
	message_display(text_to_display)

def crash():
    text_handler.message_display('You Crashed')
    obstacle.square(gameDisplay, random.randrange(0,display_width),display_height - 106)
    game_loop()
				
def game_loop():
	
	gameExit = False
	x =  (display_width * 0.45)
	y = (display_height * 0.9)
	square_x = (50)
	square_y = (50)

	#used to change where the car is on the x axis. It's used inside the game loop as an updater.
	x_change = 0

	while not gameExit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					x_change = -9
				elif event.key == pygame.K_RIGHT:
					x_change = 9
				elif event.key == pygame.K_ESCAPE:
					pygame.quit()
					quit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
					x_change = 0
		x += x_change
		square_y += 10

		gameDisplay.fill(white)
		
		obstacle.square(gameDisplay,square_x,square_y)
		race_car.rectCar(gameDisplay,x,y)
		print(obstacle.y)
		if obstacle.y > display_height:
			print ("moved")
			obstacle.move_square(gameDisplay,display_width,display_height)
		
		#checkCollision(race_car.car_image, obstacle.rect)

		#see if the y axis of the player object and the y axis of the obstacle object cross over
		
		'''if obstacle.check_colision(x,y,race_car.car_width) == True:
			crash()	
		if obstacle2.check_colision(x,y,race_car.car_width) == True:
			crash()
		if obstacle3.check_colision(x,y,race_car.car_width) == True:
			crash()'''
	
		pygame.display.update()
		clock.tick(24)		
#used to display the welcome message
gameDisplay.fill(white)
pygame.display.update()
text_handler.display_message("Welcome!")
#Activate the game loop
game_loop()
#When the game loop ends close the game
pygame.quit()
#Quit python
quit()
