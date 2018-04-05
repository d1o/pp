from sets import *

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((TILESIZE, TILESIZE))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos
		self.vel = pygame.math.Vector2((0, 0))
		self.acc = pygame.math.Vector2((0, 0))

		self.vel_x = 0
		self.vel_y = 0

		self.jumping = 0

	def update(self):
		self.acc = pygame.math.Vector2((0, GRAVITY))
		if self.jumping != 0:
			self.jumping -= 1

		k = pygame.key.get_pressed()
		if k[pygame.K_RIGHT] or k[pygame.K_d]: 
			self.acc.x = P_ACC

		if k[pygame.K_LEFT] or k[pygame.K_a]: 
			self.acc.x = -P_ACC

		if k[pygame.K_UP] or k[pygame.K_w]:
			if self.jumping == 0: 
				self.jumping = 50
				self.vel.y = -12

		self.acc.x += self.vel.x * P_FRI
		self.vel += self.acc
		self.pos += self.vel + self.acc/2
		self.rect.midbottom = self.pos