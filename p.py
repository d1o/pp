import pygame, sys, random
from pygame.locals import *
import math

class Player():
	def __init__(self, x, y):
		self.pos_x = x
		self.pos_y = y

		self.vel_x = 0
		self.vel_y = 0

		self.wait_for_jump = 0

		self.on_ground = True
		self.double_jump = False

		self.img = pygame.image.load('img/player0.png')

	def move(self):
		keys = pygame.key.get_pressed()
		player_vel_x = 0
		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			self.vel_x = -7
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.vel_x = 7
		if keys[pygame.K_SPACE]:
			if  self.on_ground and not self.double_jump and self.wait_for_jump == 0:
				self.vel_y = -25
				self.on_ground = False
				self.wait_for_jump = 15
			if  not self.on_ground and not self.double_jump and self.wait_for_jump > 0 and self.vel_y > 6:
				print('d')
				self.double_jump = True
				self.vel_y -= 25
				self.double_jump = True
				self.wait_for_jump += 15

	def draw(self, window):
		self.pos_x += self.vel_x
		self.pos_y += self.vel_y
		self.vel_x = 0
		if not self.on_ground:
			self.vel_y += 2
			if self.pos_y >= height-45:
				self.on_ground = True;
				self.double_jump = False;
				self.pos_y = height-45
				self.vel_y = 0

		if self.on_ground and self.wait_for_jump != 0:
			self.wait_for_jump -= 1
		window.blit(self.img, (self.pos_x, self.pos_y))

def jump():
	pass

width = 640
height = 480

pygame.init()
fps_clock = pygame.time.Clock()

window = pygame.display.set_mode((width, height), 0, 32)
pygame.display.set_caption('p')

pygame.mouse.set_visible(False)



player = Player(100, height-45)

while True:
	window.fill((255, 255, 255))

	player.draw(window)
	player.move()

	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()
	fps_clock.tick(50)