#Settings
import pygame
class Settings():
	"""A class to store settings"""
	
	def __init__(self):
		"""init game settings"""
		self.screen_width = 800
		self.screen_height = 500
		self.bg_color = (48,48,48)
		self.font = pygame.font.SysFont("serif", 50)
		
		self.paused = False
