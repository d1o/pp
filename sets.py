import pygame, sys, random, math
from pygame.locals import *

WIDTH = 864
HEIGHT = 544
TITLE = "game"
FPS = 50
GRAVITY = 0.5
TILESIZE = 32

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
SKY = (183,224,219)

######## USTAWIENIA GRACZA ########
P_ACC = 1
P_FRI = -0.2

######## USTAWIENIA PRZECIWNIKOW ########
E_ACC1 = -0.5

######## PREDKOSC POCISKOW ########
B_SPEED_X = 20
B_SPEED_Y = 3

######## USTAWIENIA PLATFORM ########
PL_VEL = 1.8