from sets import *

class Bullet1(pygame.sprite.Sprite):
	def __init__(self, direction, pos, who):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/oth/bullet.png')
		self.rect = self.image.get_rect()
		self.who = who

		if direction == 0:
			self.rect.center = pygame.math.Vector2((pos[0]+TILESIZE, pos[1]))
			self.vel = pygame.math.Vector2((B_SPEED_X, 0))
			
		elif direction == 1:
			self.rect.center = pygame.math.Vector2((pos[0]-TILESIZE, pos[1]))
			self.vel = pygame.math.Vector2((-B_SPEED_X, 0))

	def __del__(self):
		pass

	def update(self):
		self.rect.center += self.vel

class Bullet(pygame.sprite.Sprite):
	def __init__(self, direction, mode, pos, who):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/oth/bullet.png')
		self.rect = self.image.get_rect()
		self.who = who
		self.vel = pygame.math.Vector2((0, 0))

		if direction == 0:
			self.rect.center = pygame.math.Vector2((pos[0]+TILESIZE, pos[1]))
			self.vel.x = B_SPEED_X
			
		elif direction == 1:
			self.rect.center = pygame.math.Vector2((pos[0]-TILESIZE, pos[1]))
			self.vel.x = -B_SPEED_X

		if mode == '0':
			self.vel.y = 0
		elif mode == '1':
			self.vel.y = B_SPEED_Y
		elif mode == '2':
			self.vel.y = -B_SPEED_Y

	def __del__(self):
		pass

	def update(self):
		self.rect.center += self.vel
