#Game Functions
import sys
import pygame
import combat as comb

def events():
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			keydown(event)
		elif event.type == pygame.KEYUP:
			keyup(event)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mousex, mousey = pygame.mouse.get_pos()
			click(mousex, mousey)
			
def keydown(event):
	if event.key == pygame.K_RIGHT:
		#move guy
		example = True
	elif event.key == pygame.K_ESCAPE:
		sys.exit()	

def keyup(event):
	if event.key == pygame.K_RIGHT:
		#stop move guy
		example = True
	

def click(mousex, mousey):		
	#check collission with buttons
	example = True




def update_screen(sett, screen, dialogue_active, combat_active, dialos = None, string = "", r = 192,g = 192, b = 192):
	"""update images on the screen and flip the screen"""
	#redraw screenduring each pass of the loop
	screen.fill(sett.bg_color)
	
	if dialogue_active:
		for d in dialos:
			d.blitme()
		label = sett.font.render(string, True, (r,g,b))
		screen.blit(label, (300, 450))	
	if combat_active:
			comb.drawspots(sett, screen)	
			comb.blitme(screen)

	#if not stats.game_active:
	#	play_button.draw_button()			
				
	#make most recently drawn screen vivible		
	pygame.display.flip()

