import pygame
import random

class squareObject:

	def __init__(self, square_image, square_width, square_height,x,y):
		self.square_image = square_image
		self.square_width = square_width
		self.square_height = square_height
		self.x = x
		self.y = y
		
		
	def square(self,gameDisplay,x,y):
		
		gameDisplay.blit(self.square_image, (x,y))
		self.x = x
		self.y = y
		
	def move_square(self,gameDisplay,display_width,display_height):
		
		new_x = random.randrange(0,display_width)
		new_y = 0
		self.square(gameDisplay,new_x, new_y)
		
	def respawn_check(self,x,y,display_width,display_height):
		if y > display_height:
			self.objecty = 0 - self.objecth
			self.objectx = random.randrange(0,display_width)
			print ("object respawned")
			
	def check_colision(self,x,y, car_width):
		did_crash = False
		if y < self.objecty + self.objecth:
			print("y crossover occurred")
			if x >self.objectx and x <self.objectx + self.objectw or x+car_width > self.objectx and x + car_width < self.objectx+self.objectw:
				print("x crossover occurred")
				print("player crashed into object")
				did_crash = True
				return did_crash

class player:
	
	def __init__ (self, car_image, car_width, car_height,x,y):
		self.car_image = car_image
		self.car_width = car_width
		self.car_height = car_height
		
	def car(self,gameDisplay,x,y):
		
		gameDisplay.blit(self.car_image, (x,y))
		
	def rectCar(self,gameDisplay,x,y):
		
		gameDisplay.blit(self.car_image, (x,y))
		
		
		


