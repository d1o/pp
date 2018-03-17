from sets import *

class PBullet():
	def __init__(self, x, y, direction):
		self.bimg = pygame.image.load('img/bullet.png')
		self.shooted = 0
		
		self.pos_y = y
		if direction % 2 == 0:
			self.vel_x = 20
			self.pos_x = x + 25
		else:
			self.vel_x = -20
			self.pos_x = x - 10

		print(direction % 2)

	def draw(self, window):
		self.pos_x += self.vel_x
		window.blit(self.bimg, (self.pos_x, self.pos_y))
		self.shooted += 1
