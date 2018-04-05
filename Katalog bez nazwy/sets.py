import pygame, sys, random
from pygame.locals import *

WIDTH = 736
HEIGHT = 480
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
P_ACC = 0.5
P_FRI = -0.15