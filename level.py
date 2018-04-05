from sets import *
from blockclass import *

LVL_H = 25
LVL_W = 35

level = [
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, B1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[B1, S1, S1, B1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[B1, B2, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, B1],
	[B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, B1],
	[B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, D1, D1, D1, D1, D1, D2],
	[B2, B1, B1, B1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, D1, D3, D3, D3, D3, D3],
	[D2, D2, D2, D2, D2, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, B1, B1, B1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D3, D3, D3, D3, D3, D3],
	[D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, S1, S1, S1, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3],
	[D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D2, D2, D2, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3, D3],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, D3, D3, D3, D3, D3, D3, S1, S1, S1, S1, S1, S1, S1, S1, S1, D3, D3, D3, D3, D3],
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, D3, D3, D3, D3, D3, D3, S1, S1, S1, S1, S1, S1, S1, S1, S1, D3, D3, D3, D3, D3]
]

BLOCKS = pygame.sprite.Group()
BACKGROUND = pygame.sprite.Group()
for i in range(len(level)):
	for j in range(len(level[i])):
		if level[i][j] in colls:
			BLOCKS.add(Block(16+j*TILESIZE, 16+i*TILESIZE, level[i][j]))
		else:
			BACKGROUND.add(Block(16+j*TILESIZE, 16+i*TILESIZE, level[i][j]))