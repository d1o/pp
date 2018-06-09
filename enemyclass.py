from sets import *
from bulletclass import *

class Enemy1(pygame.sprite.Sprite):
	def __init__(self, x, y, main):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/enemies/enemy/enemy0l.png')
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos
		self.vel = pygame.math.Vector2((0, 0))
		self.acc = pygame.math.Vector2((0, 0))
		self.main = main
		self.enemy_acc = E_ACC1

		self.last_jump = 0		#odstep w czasie miedzy skokami	
		self.on_ground = True	#skok mozliwy tylko jak postac stoi na podlozu

		#wybor obrazka
		self.which_img = 0		
		self.img_dir= 'l'

	def update(self):
		#zmiana img w trakcie ruchu przeciwnika
		if self.vel.x > 0:
			self.img_dir = 'p'
		else:
			self.img_dir = 'l'

		self.which_img = (self.which_img + 1) % 8
		self.image = pygame.image.load('img/enemies/enemy/enemy'+str(self.which_img)+self.img_dir+'.png')
		self.rect = self.image.get_rect()
		self.rect.center = self.pos

		self.acc = pygame.math.Vector2((self.enemy_acc, 0))

		self.acc.x += self.vel.x * P_FRI
		self.vel.x += self.acc.x

		self.colls()

		self.pos += self.vel
		self.rect.center = self.pos

		if self.vel.y <= 15:
			self.vel.y += self.acc.y

	def colls(self):
		blocks_hit_list = pygame.sprite.spritecollide(self, self.main.cls, False)
		if blocks_hit_list:
			for s in blocks_hit_list:
				if self.rect.left < s.rect.right and self.rect.right > s.rect.right:
					self.rect.left = s.rect.right
				elif self.rect.right > s.rect.left and self.rect.left < s.rect.left:
					self.rect.right = s.rect.left
				self.vel.x *= -1
				self.enemy_acc *= -1
				
				if self.rect.bottom >= s.rect.top and self.rect.top < s.rect.top:
					self.rect.bottom = s.rect.top

##################################################

class Spikes(pygame.sprite.Sprite):
	def __init__(self, x, y, ver, main):
		pygame.sprite.Sprite.__init__(self)
		self.ver = ver
		self.image = pygame.transform.rotate(pygame.image.load('img/enemies/spikes/spikes.png'), self.ver * 90)
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos
		self.main = main

##################################################

class Turret(pygame.sprite.Sprite):
	def __init__(self, x, y, main):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/enemies/turret/turret1.png')
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos
		self.main = main

		self.wait_for_shoot = 0
		self.lives = 1

	def update(self):
		self.wait_for_shoot += 1
		if self.wait_for_shoot and math.fabs(self.main.player.pos.x - self.pos.x) < 10 * TILESIZE and self.main.player.rect.bottom <= self.rect.bottom and self.wait_for_shoot > 60:
			x = self.main.player.pos.x - self.pos.x
			y = self.main.player.pos.y - self.pos.y
			a = math.atan2(y, x)
			b = Bullet(10*math.cos(a), 10*math.sin(a), self.rect.center, 't')
			self.main.sprites.add(b)
			self.main.shots.add(b)
			self.wait_for_shoot = 0

		if self.lives != 1:
			self.image = pygame.image.load('img/enemies/turret/turret2.png')
			self.rect = self.image.get_rect()
			self.rect.center = self.pos

class Turret2(pygame.sprite.Sprite):
	def __init__(self, x, y, mode, main):
		pygame.sprite.Sprite.__init__(self)
		self.mode = int(mode)
		if self.mode == 0:
			self.image = pygame.image.load('img/enemies/turret/tu.png')
		else:
			self.image = pygame.transform.flip(pygame.image.load('img/enemies/turret/tu.png'), True, False)
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos
		self.main = main
		
		self.wait_for_shoot = 0
		self.lives = 1

	def update(self):
		self.wait_for_shoot += 1
		if self.wait_for_shoot > 75:
			if self.mode == 0:
				b = Bullet(-B_SPEED_X/2, 0, self.rect.center, 't')
			else:
				b = Bullet(B_SPEED_X/2, 0, self.rect.center, 't')
			self.main.sprites.add(b)
			self.main.shots.add(b)
			self.wait_for_shoot = 0

		if self.lives != 1:
			if self.mode == 0:
				self.image = pygame.image.load('img/enemies/turret/tu2.png')
			else:
				self.image = pygame.transform.flip(pygame.image.load('img/enemies/turret/tu2.png'), True, False)

			self.rect = self.image.get_rect()
			self.rect.center = self.pos