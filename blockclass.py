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