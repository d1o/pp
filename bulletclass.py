from sets import *

class Bullet1(pygame.sprite.Sprite):
	def __init__(self, direction, pos, who):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/oth/bullet.png')
		self.rect = self.image.get_rect()
		self.who = who

		if direction > 0:
			self.rect.center = pygame.math.Vector2((pos[0]+TILESIZE, pos[1]))
			self.vel = pygame.math.Vector2((B_SPEED, 0))
			
		elif direction < 0:
			self.rect.center = pygame.math.Vector2((pos[0]-TILESIZE, pos[1]))
			self.vel = pygame.math.Vector2((-B_SPEED, 0))

	def __del__(self):
		pass

	def update(self):
		self.rect.center += self.vel

class Bullet2(pygame.sprite.Sprite):
	def __init__(self, direction, pos, who):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/oth/bullet.png')
		self.rect = self.image.get_rect()
		self.who = who

		if direction > 0:
			self.rect.center = pygame.math.Vector2((pos[0]+TILESIZE, pos[1]))
			self.vel = pygame.math.Vector2((B_SPEED, 0))
			
		elif direction < 0:
			self.rect.center = pygame.math.Vector2((pos[0]-TILESIZE, pos[1]))
			self.vel = pygame.math.Vector2((-B_SPEED, 0))

	def __del__(self):
		pass

	def update(self):
		self.rect.center += self.vel
