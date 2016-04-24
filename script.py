#Aidan Melchior
#MAIN game file
import pygame
import sys
from pygame.sprite import Group

from Settings import Settings
from dialogue import Dialogue

import GameFunct as gf
		
def test(sett, screen):	
	pepe = pygame.image.load('pepe.png')				
	borrito = pygame.image.load('borrito.png')				 
	test_dia = Dialogue(sett, screen, "right", "", pepe)
	test_dia2 = Dialogue(sett,screen, "left", "", borrito)

	dials = Group()
	dials.add(test_dia)
	dials.add(test_dia2)
		
	backwards = False

	while True:
		gf.events()
	
		if not sett.paused:
			test_dia.update(backwards)
			test_dia2.update(backwards)
			print(test_dia2.x)
			if test_dia.x == 100:
			##test dialogue. TODO have file of encounters to refer to 
				
				gf.update_screen(sett, screen, True, dials,"i am here to slay",173,255,47)
				pygame.time.wait(3000)
				gf.update_screen(sett, screen, True, dials,"prepare urself",173,255,47)
				pygame.time.wait(3000)
				gf.update_screen(sett, screen, True, dials,"no way",255,69,0)
				pygame.time.wait(3000)
				backwards = True
				#test_dia.x = test_dia.x -1  #back()
				#test_dia2.x= test_dia2.x +1 #back()
				
			if test_dia.x < -200:
				del test_dia
			if test_dia2.x > 800:	
				del test_dia2
				dials.empty()
									
		gf.update_screen(sett, screen, True, dials)
				
def combat(level):
	inte = 0
