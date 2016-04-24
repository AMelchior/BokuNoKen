#Aidan Melchior
#MAIN game file
import pygame
import sys
from pygame.sprite import Group

from character import Character
from Settings import Settings
from dialogue import Dialogue
import script as scr
import GameFunct as gf
import combat as comb

def run_game():
	pygame.init()
	sett = Settings()
	screen = pygame.display.set_mode((sett.screen_width, 
									  sett.screen_height))
	pygame.display.set_caption("video game :^)")
	
	me = Character()
	
	#pause = False #eventually start game paused
	#moved to settings.py
	###scr.test(sett,screen)	
	scr.combat(10)	
	comb.spawn(me, 5)
	while True:						#dialogue, combat	
		gf.update_screen(sett, screen, False,   True)	
run_game()		
