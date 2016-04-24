#VN type dialogue
import pygame
from pygame.sprite import Sprite

class Dialogue(Sprite):
	"""pop up dialogue in the game"""
	#TODO pause game
	
	def __init__(self, settings, screen, direction, string, image):
		super(Dialogue,self).__init__()
		self.screen = screen
		self.settings = settings
		self.direction = direction #left(from right) or right (from left)
		self.string = string #actual dialogue
		self.font = settings.font
		self.label = self.font.render(string, True, (136,136,136))
		
		self.screenright = settings.screen_width
		self.screenleft = 0
		self.screentop = 0
		self.screenbottom = settings.screen_height
		
		self.left = 'left'
		self.right = 'right'
		
		#load img
		self.image = image
		self.rect = self.image.get_rect()

		#starting pos
		#self.rect.x = 0#self.rect.width
		self.rect.y = 100#self.rect.height
		
		#adjusting pos based on start (mc direction = right, starts left)
		if self.direction == self.right:
			self.rect.x =-200
			
		else: #if left, starts to the right
			self.rect.x = 800

		
		#store postition
		self.x = float(self.rect.x)
		
	def blitme(self):
		self.screen.blit(self.image, self.rect)	

			
	def update(self, back):
		"""move icon towards center of screen for 100px"""
		if self.direction == self.left:#moving left
			if self.x > self.screenright - 200 and not back:
				self.x = self.x -1
			if self.x < self.screenright and back:
				self.x = self.x +1
		else:#moving right
			if self.x < self.screenleft + 100 and not back:
				self.x = self.x +1
			if self.x > self.screenleft - 200 and back:
				self.x = self.x -1
			
		self.rect.x = self.x	
		
