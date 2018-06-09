from sets import *

class Background(pygame.sprite.Sprite):
	def __init__(self, x, y, l):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/levels/bg' + str(l) + '.png')
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.topleft = self.pos