import pygame, sys, random
from pygame.locals import *

WIDTH = 832
HEIGHT = 576
TITLE = "game"
FPS = 50
GRAVITY = 0.5
TILESIZE = 32

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)

######## USTAWIENIA GRACZA ########
P_ACC = 1
P_FRI = -0.2

########  ########
B_SPEED = 25

######## GRAFIKI ########
D1 = pygame.image.load('img/tiles/dirt1.png')
D2 = pygame.image.load('img/tiles/dirt2.png')
D3 = pygame.image.load('img/tiles/dirt3.png')
B1 = pygame.image.load('img/tiles/bricks1.png')
B2 = pygame.image.load('img/tiles/bricks2.png')
S1 = pygame.image.load('img/tiles/sky1.png')

colls = [D1, D2, D3, B1, B2]
no_colls = [S1]