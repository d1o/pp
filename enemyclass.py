from sets import *

class Enemy1(pygame.sprite.Sprite):
	def __init__ (self, x, y, BLCKS):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.Surface((TILESIZE, TILESIZE))
		self.image.fill(RED)
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos
		self.vel = pygame.math.Vector2((0, 0))
		self.acc = pygame.math.Vector2((0, 0))

		self.BLOCKS = BLCKS

		self.vel_x = 0
		self.vel_y = 0

		self.jumping = False
		self.last_jump = 0

		self.shooting = False		#gdy True to wywołuje funkcje w game.py
		self.wait_for_shoot = 0		#ograniczenie strzelania w czasie
		self.last_dir = 1			#kierunek w jakim poleci pocisk


	def update(self):
		self.acc.x = 0
		self.acc.y = GRAVITY

		#zatrzymywanie gracza w miejscu
		if abs(self.vel.x) < 0.01:
			self.vel.x = 0

		#w powietrzu opory są większe by łatwiej starować postacią
		self.p_fric = P_FRI
		if self.jumping and self.last_jump != 0:
			self.p_fric *= 3

		#wieksze tarcie na poczatku ruchu
		if (self.vel.x < 2*P_ACC and self.acc.x > 0) or (self.vel.x > -2*P_ACC and self.acc.x < 0):
			self.additional_fric = self.p_fric
		else:
			self.additional_fric = 0

		#tarcie
		self.acc.x += self.vel.x * (self.p_fric + self.additional_fric)
		self.vel.x += self.acc.x
		if self.vel.y <= 15:
			self.vel.y += self.acc.y
		self.wall_collision()
		if self.vel.x != self.last_dir and self.vel.x != 0: 
			self.last_dir = self.vel.x
		self.pos += self.vel
		self.rect.center = self.pos

		#ograniczenie skoków w czasie
		if self.last_jump != 0:
			self.last_jump -= 1


	def wall_collision(self):
		#if self.rect.left + self.vel.x <= 0:
		#	self.vel.x = 0

		for b in self.BLOCKS:
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
					if self.jumping and self.last_jump == 0:
						self.vel.y -= 12
						self.last_jump = 60
						self.jumping = False
					elif not self.jumping and self.last_jump > 15:
						self.last_jump = 15

				#kolizja góry
				elif self.rect.top + self.vel.y <= b.rect.bottom and self.rect.top + self.vel.y > b.rect.top:
					self.vel.y = (b.rect.bottom - self.rect.top)