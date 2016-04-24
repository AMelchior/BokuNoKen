from random import randint
from enemy import Enemy
from character import Character

#32wx20h
a = [[0 for x in range(20)] for x in range(32)] #store positions
#print(a)
b = [[0 for x in range(20)] for x in range(32)] #store x,y value

enem = Enemy(0)
horde = [enem]
me = Character()

for y in range(500):
	if y%25 == 0 and y!= 0:
		print('y')
		print(y)
		for x in range (800):
			if x % 25 == 0 and x !=0:
				print(x)
				b[(x/25) - 1][(y/25) - 1] = (x,y)
print(b[0])	
for w in range(20):
	print(b[w])
		

def drawspots(sett, screen):
	label = sett.font.render('+', True, (198,198,198))
	for y in range(20):
		for x in range(32):
			if not b[x][y] == 0:
				screen.blit(label, b[x][y])



def spawn(me, num_enemies):
	for e in range(num_enemies):
		x = randint(0,31)
		y = randint(0,19)
		if a[x][y] is 0:
			a[x][y] = 1
			monster = Enemy(me.lv)
			horde.append(monster)
			print('horde', b[x][y])
			horde[e].rect.center = b[x][y]
			
	#print('*************')		
	#print(a)
	if a[10][16] is 0:
		a[10][16] = 1
		print('me', b[10][16])
		me.rect.center = 200,200#b[10][16]
		
	
	
def blitme(screen):
	for enemy in horde:
		enemy.blitme(screen)
	me.blitme(screen)	 
		
	
