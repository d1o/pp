from sets import *

class Bonus(pygame.sprite.Sprite):
	def __init__(self, pos):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/oth/bns.png')
		self.rect = self.image.get_rect()
		self.rect.center = pos
