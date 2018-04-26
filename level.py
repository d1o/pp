from sets import *
from blockclass import *
from enemyclass import *

LVL_H = 25
LVL_W = 35

level = [
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, B1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1],
	[D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3],
	[D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4],
	[D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4],
	[S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4, D4],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[B1, B2, D3, D3, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, B2, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1],
	[B1, B2, D3, D3, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, B2, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1],
	[B1, B2, D3, D3, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, B2, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1],
	[B1, B2, D3, D3, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, B2, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1],
	[B1, B2, D3, D3, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, B2, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1],
	[B1, B2, D3, D3, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, B2, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1]

]
print(len(level))

BLOCKS = pygame.sprite.Group()
BACKGROUND = pygame.sprite.Group()
E = [(700,272)]
for i in range(len(level)):
	for j in range(len(level[i])):
		if level[i][j] in colls:
			BLOCKS.add(Block(16+j*TILESIZE, 16+i*TILESIZE, level[i][j]))
		elif level[i][j] in no_colls:
			BACKGROUND.add(Block(16+j*TILESIZE, 16+i*TILESIZE, level[i][j]))
		elif level[i][j] in enems:
			E.append((j,i))