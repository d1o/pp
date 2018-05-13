from sets import *

class Pnt(pygame.sprite.Sprite):
	def __init__(self):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/oth/pnt.png')
		#self.image.fill(color)
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((0, 0))
		self.rect.center = self.pos