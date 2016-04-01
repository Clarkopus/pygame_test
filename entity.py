import pygame
import random


class squareObject:

	def __init__(self,objectx, objecty, objectw, objecth, object_speed, color):
		self.objectx = objectx
		self.objecty = objecty
		self.object_speed = object_speed
		self.objectw = objectw
		self.objecth = objecth
		self.color = color
		
		
	def draw_object_rec(self,gameDisplay):
		pygame.draw.rect(gameDisplay, (0,0,0), [self.objectx, self.objecty, self.objectw, self.objecth])
		
	def respawn_check(self,x,y,display_height,display_width):
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
		


