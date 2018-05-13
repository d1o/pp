from sets import *
from blockclass import *
from enemyclass import *

D1 = pygame.image.load('img/tiles/dirt1.png')
D2 = pygame.image.load('img/tiles/dirt2.png')
D3 = pygame.image.load('img/tiles/dirt3.png')
D4 = pygame.image.load('img/tiles/dirt4.png')
B1 = pygame.image.load('img/tiles/bricks1.png')
B2 = pygame.image.load('img/tiles/bricks2.png')
S1 = pygame.image.load('img/tiles/sky1.png')
BO = pygame.image.load('img/tiles/box11.png')
E1 = ''

colls = [D1, D2, D3, D4, B1, B2]
destroyable = [BO]
no_colls = [S1]
enems = [E1]

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
	[S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, B1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1, S1],
	[D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D2, D1, D1, D1, D1, D1, D1, D1, D1, B2, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1, D1],
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

BLOCKS = pygame.sprite.Group()
BOXES = pygame.sprite.Group()
BACKGROUND = pygame.sprite.Group()
E = [(750,200), (1082,200)]
S = [(1050,272), (1210,272)]
B = [(718,272), (16,208), (16,240), (16,272), (48,272), (80,272)]
for i in range(len(level)):
	for j in range(len(level[i])):
		if level[i][j] in colls:
			BLOCKS.add(Block(16+j*TILESIZE, 16+i*TILESIZE, level[i][j]))
		elif level[i][j] in no_colls:
			BACKGROUND.add(Block(16+j*TILESIZE, 16+i*TILESIZE, level[i][j]))
		elif level[i][j] in destroyable:
			BOXES.add(Box(16+j*TILESIZE, 16+i*TILESIZE, level[i][j]))