import pygame

class Character():
	def __init__(self):	
		#base stats	
		self.lv = 0	#gain xp based on damage done. enemies acculate bonus xp based on how much damage they do. 
		self.atk = 10
		self.atkxp = 0
		self.atkxpneeded = 100
		self.intel = 0
		self.intxp = 0
		self.intxpneeded = 100
		self.hp = 100
		self.hpxp = 0
		self.hpxpneeded = 100
		self.image = pygame.image.load("pepe.png")
		self.sprite =  pygame.image.load('pepe_sprite.png')
		self.speed = 5
		
		self.rect = self.image.get_rect()
		self.x = self.rect.x
		self.center = self.rect.center
		
	#	position = (0,0)
		
	def setx(newx):
		self.x = newx
		self.rect.x = newx
		
	def blitme(self, screen):
		screen.blit(self.sprite, (self.x, self.rect.y))
