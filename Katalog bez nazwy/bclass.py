from sets import *

class Block(pygame.sprite.Sprite):
	def __init__(self, x, y, color):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((TILESIZE, TILESIZE))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.rect.center = pygame.math.Vector2((x, y))