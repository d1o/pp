from sets import *

class Bullet(pygame.sprite.Sprite):
	def __init__(self, dir_x, dir_y, pos, who):
		pygame.sprite.Sprite.__init__(self)
		if who == 'p':
			self.image = pygame.image.load('img/oth/bulletp.png')
		elif who == 't':
			self.image = pygame.image.load('img/oth/bullett.png')
			
		self.rect = self.image.get_rect()
		self.who = who
		self.vel = pygame.math.Vector2((0, 0))

		if who != 't':
			if dir_x > 0:
				self.rect.center = pygame.math.Vector2((pos[0]+TILESIZE, pos[1]))
				
			elif dir_x <= 0:
				self.rect.center = pygame.math.Vector2((pos[0]-TILESIZE, pos[1]))
		else:
			self.rect.center = pos

		self.vel.x = dir_x
		self.vel.y = dir_y

	def update(self):
		self.rect.center += self.vel
