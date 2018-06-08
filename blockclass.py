from sets import *

class Block(pygame.sprite.Sprite):
	def __init__(self, x, y, img):
		pygame.sprite.Sprite.__init__(self)
		if img =='D1':
			self.path = 'img/tiles/ground/d1.png'
		elif img == 'D2':
			self.path = 'img/tiles/ground/d2.png'
		elif img == 'D3':
			self.path = 'img/tiles/ground/d3.png'
		elif img == 'B1':
			self.path = 'img/tiles/bricks/b1.png'
		elif img == 'B2':
			self.path = 'img/tiles/bricks/b2.png'
		elif img == 'WO':
			self.path = 'img/tiles/wood/wo.png'
		elif img == 'JU':
			self.path = 'img/oth/jumps.png'

		self.image = pygame.image.load(self.path)
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos

##################################################

class Box(pygame.sprite.Sprite):
	def __init__(self, x, y, main):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/tiles/box/bo1.png')
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos
		self.shots = 0
		self.main = main

		self.vel = pygame.math.Vector2((0, 0))
		self.acc = pygame.math.Vector2((0, 0))

	def update(self):
		if self.shots == 1:
			self.image = pygame.image.load('img/tiles/box/bo2.png')
		if self.shots >= 2:
			self.image = pygame.image.load('img/tiles/box/bo3.png')
		self.rect = self.image.get_rect()
		self.rect.center = self.pos

		self.acc = pygame.math.Vector2((0, GRAVITY))
		if self.vel.y <= 15:
			self.vel.y += self.acc.y

		self.pos += self.vel

		self.colls()
		self.rect.center = self.pos

	def colls(self):
		for b in self.main.cls:
			if (b.rect.right > self.rect.left and b.rect.left < self.rect.right) or \
			(b.rect.left < self.rect.right and b.rect.right > self.rect.right) or \
			(b.rect.right == self.rect.right and b.rect.left == self.rect.left):
				#kolizja spodu
				if self.rect.bottom + self.vel.y >= b.rect.top and self.rect.bottom + self.vel.y < b.rect.bottom:
					self.vel.y = -GRAVITY

##################################################

class Platform(pygame.sprite.Sprite):
	def __init__(self, x, y, mode, main):
		pygame.sprite.Sprite.__init__(self)
		if mode == 'DP':
			self.image = pygame.image.load('img/tiles/platforms/dirtpla.png')
		elif mode == 'BP':
			self.image = pygame.image.load('img/tiles/platforms/brickspla.png')
		elif mode == 'WP':
			self.image = pygame.image.load('img/tiles/platforms/wp.png')
			
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos
		self.main = main
		self.v = PL_VEL

	def update(self):
		self.vel = pygame.math.Vector2((self.v, 0))
		self.pos += self.vel
		self.rect.center = self.pos

		self.colls()

	def colls(self):
		blocks_hit_list = pygame.sprite.spritecollide(self, self.main.blocks, False)
		if blocks_hit_list:
			self.v *= -1

##################################################

class Doors(pygame.sprite.Sprite):
	def __init__(self, x, y, main):
			pygame.sprite.Sprite.__init__(self)
			self.image = pygame.image.load('img/oth/do.png')
			self.rect = self.image.get_rect()
			self.pos = pygame.math.Vector2((x, y))
			self.rect.topleft = self.pos
			self.main = main
			self.opened = False