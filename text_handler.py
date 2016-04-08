import pygame
import time

class textHandler:
	
	def __init__ (self,display_width,display_height, gameDisplay):
		
		self.display_width = display_width
		self.display_height = display_height
		self.gameDisplay = gameDisplay

	def text_objects(self,text, font):
		
		textSurface = font.render(text, True, (0,0,0))
		return textSurface, textSurface.get_rect()

	def message_display(self,text):
		
		largeText = pygame.font.Font('freesansbold.ttf',115)
		TextSurf, TextRect = self.text_objects(text, largeText)
		TextRect.center = ((self.display_width/2),(self.display_height/2))
		self.gameDisplay.blit(TextSurf, TextRect)
		pygame.display.update()
		time.sleep(2)
		  
	#custom function to create messages on the screen   
	def display_message(self,text_to_display):
		
		self.message_display(text_to_display)
