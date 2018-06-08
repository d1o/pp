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

		self.acc = pygame.math.Vector2((self.enemy_acc, GRAVITY))

		self.acc.x += self.vel.x * P_FRI
		self.vel.x += self.acc.x

		self.colls()

		self.pos += self.vel
		self.rect.center = self.pos

		if self.vel.y <= 15:
			self.vel.y += self.acc.y

		if self.on_ground and self.last_jump > 0:
			self.last_jump -= 1

	def colls(self):
		for b in self.main.cls:
			if (b.rect.bottom > self.rect.top and b.rect.bottom < self.rect.bottom) or \
			(b.rect.top < self.rect.bottom and b.rect.bottom > self.rect.bottom) or \
			(b.rect.bottom == self.rect.bottom and b.rect.top == self.rect.top):
				#kolizja prawego boku
				if self.rect.right + self.vel.x >= b.rect.left and self.rect.right + self.vel.x < b.rect.right:
					self.vel.x = (b.rect.left - self.rect.right)
					self.enemy_acc *= -1

				#kolizja lewego boku
				elif self.rect.left + self.vel.x <= b.rect.right and self.rect.left + self.vel.x > b.rect.left:
					self.vel.x = (b.rect.right - self.rect.left)
					self.enemy_acc *= -1

			
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