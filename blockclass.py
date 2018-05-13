from sets import *

class Block(pygame.sprite.Sprite):
	def __init__(self, x, y, img):
		pygame.sprite.Sprite.__init__(self)
		self.image = img
		#self.image = pygame.image.load(img)
		#self.image.fill(color)
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos

class Box(pygame.sprite.Sprite):
	def __init__(self, x, y, main):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/tiles/box11.png')
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos
		self.shots = 0
		self.main = main

		self.vel = pygame.math.Vector2((0, 0))
		self.acc = pygame.math.Vector2((0, 0))

	def update(self):
		if self.shots == 1:
			self.image = pygame.image.load('img/tiles/box12.png')
		if self.shots >= 2:
			self.image = pygame.image.load('img/tiles/box13.png')
		self.rect = self.image.get_rect()
		self.rect.center = self.pos

		self.acc = pygame.math.Vector2((0, GRAVITY))
		if self.vel.y <= 15:
			self.vel.y += self.acc.y

		self.pos += self.vel

		self.colls()
		self.rect.center = self.pos

	def colls(self):
		for b in self.main.blocks:
			if (b.rect.right > self.rect.left and b.rect.left < self.rect.right) or \
			(b.rect.left < self.rect.right and b.rect.right > self.rect.right) or \
			(b.rect.right == self.rect.right and b.rect.left == self.rect.left):
				#kolizja spodu
				if self.rect.bottom + self.vel.y >= b.rect.top and self.rect.bottom + self.vel.y < b.rect.bottom:
					self.vel.y = -GRAVITY

		for b in self.main.boxes:
			if (b.rect.right > self.rect.left and b.rect.left < self.rect.right) or \
			(b.rect.left < self.rect.right and b.rect.right > self.rect.right) or \
			(b.rect.right == self.rect.right and b.rect.left == self.rect.left):
				#kolizja spodu
				if self.rect.bottom + self.vel.y >= b.rect.top and self.rect.bottom + self.vel.y < b.rect.bottom:
					self.vel.y = -GRAVITY