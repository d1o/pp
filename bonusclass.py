from sets import *

class Bonus(pygame.sprite.Sprite):
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