from sets import *

class Bonus(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/oth/bns.png')
		self.rect = self.image.get_rect()
		self.rect.center = pos

		#liczba punktow za pdoniesienie
		self.pts = 50

class Key(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/oth/key.png')
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x,y))
		self.rect.center = self.pos

class Weapon(pygame.sprite.Sprite):
	def __init__(self, pos, v):
		pygame.sprite.Sprite.__init__(self)
		self.v = v		#jaka bron w bonusie
		if self.v == 1:
			self.image = pygame.image.load('img/oth/w1.png')
		if self.v == 2:
			self.image = pygame.image.load('img/oth/w2.png')
		self.rect = self.image.get_rect()
		self.rect.center = pos

class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y, txt):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/oth/c1.png')
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos
		self.pts = int(txt[1]) * 100
		self.which_img = random.randint(0,40)

	def update(self):
		self.which_img += 1
		if self.which_img >= 100 and self.which_img < 102:
			self.image = pygame.image.load('img/oth/c2.png')
			self.rect = self.image.get_rect()
			self.rect.center = self.pos
		elif self.which_img >= 102 and self.which_img < 104:
			self.image = pygame.image.load('img/oth/c3.png')
			self.rect = self.image.get_rect()
			self.rect.center = self.pos
		elif self.which_img >= 104 and self.which_img < 106:
			self.image = pygame.image.load('img/oth/c4.png')
			self.rect = self.image.get_rect()
			self.rect.center = self.pos
		elif self.which_img >= 106 and self.which_img < 108:
			self.image = pygame.image.load('img/oth/c5.png')
			self.rect = self.image.get_rect()
			self.rect.center = self.pos
		elif self.which_img >= 108 and self.which_img < 110:
			self.image = pygame.image.load('img/oth/c6.png')
			self.rect = self.image.get_rect()
			self.rect.center = self.pos		
		elif self.which_img >= 112:
			self.image = pygame.image.load('img/oth/c1.png')
			self.rect = self.image.get_rect()
			self.rect.center = self.pos
			self.which_img = 0
