import pygame
import random


class thing:

	def __init__(self,thingx, thingy, thingw, thingh, thing_speed, color):
		self.thingx = thingx
		self.thingy = thingy
		self.thing_speed = thing_speed
		self.thingw = thingw
		self.thingh = thingh
		self.color = color
		
		
	def draw_thing_rec(self,gameDisplay):
		pygame.draw.rect(gameDisplay, (0,0,0), [self.thingx, self.thingy, self.thingw, self.thingh])
		
	def respawn_check(self,x,y,display_height,display_width):
		if y > display_height:
			y = 10 - self.thingh
			x = random.randrange(0,display_width)
			print ("object respawned")
			
	def check_colision(self,x,y, car_width):
		did_crash = False
		if y < self.thingy + self.thingh:
			print("y crossover occurred")
			if x >self.thingx and x <self.thingx + self.thingw or x+car_width > self.thingx and x + car_width < self.thingx+self.thingw:
				print("x crossover occurred")
				print("player crashed into object")
				did_crash = True
				return did_crash
		


