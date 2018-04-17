from sets import *

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, main):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((TILESIZE, TILESIZE))
		self.image.fill(GREEN)
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos
		self.vel = pygame.math.Vector2((0, 0))
		self.acc = pygame.math.Vector2((0, 0))
		self.main = main

		self.last_jump = 0		#odstep w czasie miedzy skokami	
		self.on_ground = True	#skok mozliwy tylko jak postac stoi na podlozu

	def update(self):
		self.acc = pygame.math.Vector2((0, GRAVITY))
		self.control()

		if abs(self.vel.x) < 0.01:
			self.vel.x = 0

		self.acc.x += self.vel.x * P_FRI
		self.vel.x += self.acc.x

		self.colls()

		self.pos += self.vel
		self.rect.center = self.pos

		if self.vel.y <= 15:
			self.vel.y += self.acc.y

		if self.on_ground and self.last_jump > 0:
			self.last_jump -= 1

		print(self.vel.y, self.last_jump, self.acc.y, self.on_ground)

	def control(self):
		k = pygame.key.get_pressed()
		if k[pygame.K_RIGHT] or k[pygame.K_d]: 
			self.acc.x = P_ACC
		if k[pygame.K_LEFT] or k[pygame.K_a]: 
			self.acc.x = -P_ACC
		if (k[pygame.K_UP] or k[pygame.K_w]):
			self.jump()
		if (k[pygame.K_DOWN] or k[pygame.K_s]):
			pass
		if (k[pygame.K_SPACE])	 and self.wait_for_shoot == 0:
			pass

	def colls(self):
		for b in self.main.blocks:
			if (b.rect.bottom > self.rect.top and b.rect.bottom < self.rect.bottom) or \
			(b.rect.top < self.rect.bottom and b.rect.bottom > self.rect.bottom) or \
			(b.rect.bottom == self.rect.bottom and b.rect.top == self.rect.top):
				#kolizja prawego boku
				if self.rect.right + self.vel.x >= b.rect.left and self.rect.right + self.vel.x < b.rect.right:
					self.vel.x = (b.rect.left - self.rect.right)

				#kolizja lewego boku
				elif self.rect.left + self.vel.x <= b.rect.right and self.rect.left + self.vel.x > b.rect.left:
					self.vel.x = (b.rect.right - self.rect.left)

			
			elif (b.rect.right > self.rect.left and b.rect.left < self.rect.right) or \
			(b.rect.left < self.rect.right and b.rect.right > self.rect.right) or \
			(b.rect.right == self.rect.right and b.rect.left == self.rect.left):
				#kolizja spodu
				if self.rect.bottom + self.vel.y >= b.rect.top and self.rect.bottom + self.vel.y < b.rect.bottom:
					self.vel.y = (b.rect.top - self.rect.bottom)
					if not self.on_ground and self.vel.y >= 0:
						self.on_ground = True

				#kolizja góry
				elif self.rect.top + self.vel.y <= b.rect.bottom and self.rect.top + self.vel.y > b.rect.top:
					self.vel.y = (b.rect.bottom - self.rect.top)

	def jump(self):
		if self.on_ground and self.last_jump == 0:
			self.on_ground = False
			self.vel.y = -12
			self.last_jump = 15