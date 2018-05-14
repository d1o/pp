from sets import *

class Bonus(pygame.sprite.Sprite):
	#dodatkowe punkty
	def __init__(self, pos, who):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/oth/bns.png')
		self.rect = self.image.get_rect()
		self.rect.center = pos

		#liczba punktow za pdoniesienie
		if who == 'box':
			self.pts = 50
		elif who == 'enemy':
			self.pts = 100

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