import pygame
import time
import random
import entity

pygame.init()

display_width = 1000
display_height = 900

#set the display to be 800 x 600
gameDisplay = pygame.display.set_mode((display_width,display_height))
#set the display caption
pygame.display.set_caption('Dodge shit get hit')

black = (0,0,0)
white = (255,255,255)
#create a pygame clock to keep track of time
clock = pygame.time.Clock()

race_car = entity.player(pygame.image.load('racecar.png'), 73, 82 , display_width*0.45, display_height*0.8)
#used to place where the car is going to be
obstacle = entity.squareObject(random.randrange(0,display_width),-600,100,100,20, (0,0,0))
obstacle2 = entity.squareObject(random.randrange(0,display_width),-600,100,100,17, (0,0,0))
obstacle3 = entity.squareObject(random.randrange(0,display_width),-600,100,100,18, (0,0,0))

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
    obstacle.objecty -=display_height
    obstacle.objectx = random.randrange(0,(display_width - obstacle.objectw))
    obstacle2.objecty -=display_height
    obstacle2.objectx = random.randrange(0,(display_width - obstacle2.objectw))
    obstacle3.objecty -=display_height
    obstacle3.objectx = random.randrange(0,(display_width - obstacle3.objectw))
    game_loop()
		
			
def game_loop():
	
	gameExit = False
	x =  (display_width * 0.45)
	y = (display_height * 0.9)

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

		gameDisplay.fill(white)
		
		obstacle.draw_object_rec(gameDisplay)
		obstacle2.draw_object_rec(gameDisplay)
		obstacle3.draw_object_rec(gameDisplay)
		obstacle.objecty += obstacle.object_speed
		obstacle2.objecty += obstacle2.object_speed
		obstacle3.objecty += obstacle3.object_speed
		obstacle.respawn_check(obstacle.objectx, obstacle.objecty,display_height, display_width)
		obstacle2.respawn_check(obstacle2.objectx, obstacle2.objecty, display_height, display_width)
		obstacle3.respawn_check(obstacle3.objectx, obstacle3.objecty, display_height, display_width)
		
		race_car.car(gameDisplay,x,y)

		#see if the y axis of the player object and the y axis of the obstacle object cross over
		if obstacle.check_colision(x,y,race_car.car_width) == True:
			crash()	
		if obstacle2.check_colision(x,y,race_car.car_width) == True:
			crash()
		if obstacle3.check_colision(x,y,race_car.car_width) == True:
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
