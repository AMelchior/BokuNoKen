from random import randint
import pygame


class Enemy():
	
	def __init__(self,level):
		self.lv = level
		self.atk = 10 + randint(0,self.lv)
		self.hp = randint (80, 	100 + self.lv) 
		self.speed = 4	
		self.bonusxp = 0
		self.image = pygame.image.load('borrito.png')
		self.sprite = pygame.image.load('skelly.png')
		self.rect = self.image.get_rect()
		self.center = self.rect.center
		
	def blitme(self, screen):
		screen.blit(self.sprite, self.rect)
