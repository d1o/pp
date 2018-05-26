from sets import *
from bulletclass import *

class Player(pygame.sprite.Sprite):
	def __init__(self, x, y, main):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('img/player/player1p.png')
		self.rect = self.image.get_rect()
		self.pos = pygame.math.Vector2((x, y))
		self.rect.center = self.pos
		self.vel = pygame.math.Vector2((0, 0))
		self.acc = pygame.math.Vector2((0, 0))
		self.main = main

		self.last_jump = 0		#odstep w czasie miedzy skokami	
		self.on_ground = True	#skok mozliwy tylko jak gracz stoi na podlozu

		self.last_shot = 0		#odstep strzelania w czasie
		self.last_direction = 0	#kierunek w ktorym obrocony jest gracz
		self.weapon = 1 		#ktora bron uzywa gracz

		self.which_img = 0		#wybor obrazka

	def update(self):
		self.acc = pygame.math.Vector2((0, GRAVITY))
		self.controls()

		#zatrzymywanie postaci w miejscu
		if abs(self.vel.x) < 0.01:
			self.vel.x = 0

		#gdy gracz stoi w miejscu zmiana img na poczatkowy
		if self.vel.x == 0:
			if self.last_direction == 0:
				self.image = pygame.image.load('img/player/player0p.png')
				self.rect = self.image.get_rect()
				self.rect.center = self.pos
			else:
				self.image = pygame.image.load('img/player/player0l.png')
				self.rect = self.image.get_rect()
				self.rect.center = self.pos

		#obliczanie kroku
		self.acc.x += self.vel.x * P_FRI
		self.vel.x += self.acc.x

		self.colls()

		self.pos += self.vel
		self.rect.center = self.pos

		#przyspieszenie grawitacyjne
		if self.vel.y <= 15:
			self.vel.y += self.acc.y

		#zerowanie oczekawinia na strzal i skok
		if self.on_ground and self.last_jump > 0:
			self.last_jump -= 1
		if self.last_shot > 0:
			self.last_shot -= 1

	def controls(self):
		k = pygame.key.get_pressed()
		if k[pygame.K_RIGHT] or k[pygame.K_d]: 
			self.acc.x = P_ACC

			#zmiana img w trakcie ruchu gracza
			if self.last_direction == 1:
				self.which_img = 0
			elif self.last_direction == 0 and self.on_ground == True:
				self.which_img = (self.which_img + 1) % 8

			self.image = pygame.image.load('img/player/player'+str(self.which_img)+'p.png')
			self.rect = self.image.get_rect()
			self.rect.center = self.pos

			self.last_direction = 0
			
		if k[pygame.K_LEFT] or k[pygame.K_a]: 
			self.acc.x = -P_ACC

			#zmiana img w trakcie ruchu gracza
			if self.last_direction == 0:
				self.which_img = 0
			elif self.last_direction == 1 and self.on_ground == True:
				self.which_img = (self.which_img + 1) % 8

			self.image = pygame.image.load('img/player/player'+str(self.which_img)+'l.png')
			self.rect = self.image.get_rect()
			self.rect.center = self.pos

			self.last_direction = 1

		if (k[pygame.K_UP] or k[pygame.K_w]):
			self.jump()
		if (k[pygame.K_DOWN] or k[pygame.K_s]):
			pass
		if (k[pygame.K_SPACE]):
			self.shoot()

		if (k[pygame.K_1]):
			self.weapon = 1
		if (k[pygame.K_2]):
			self.weapon = 2

	def colls(self):
		######## KOLIZJE ZE ŚCIANAMI ########
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

		######## KOLIZJE ZE SKRZYNKAMI ########
		for b in self.main.boxes:
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


		######## KOLIZJE Z KOLCAMI ########
		for s in self.main.spikes:
			#kolizje od góry
			if s.ver == 0 and ( (s.rect.top == self.rect.bottom) or (s.rect.top < self.rect.bottom and s.rect.top > self.rect.top) ) and ( (s.rect.left > self.rect.left and s.rect.left < self.rect.right) or (s.rect.left == self.rect.left and s.rect.right == self.rect.right) or (s.rect.left < self.rect.left and s.rect.right > self.rect.left) ):
				self.main.game = False

			if s.ver == 1 and ( (s.rect.left == self.rect.right) or (s.rect.left < self.rect.right and s.rect.right > self.rect.left) ) and ( (s.rect.bottom > self.rect.bottom and s.rect.top < self.rect.bottom) or (s.rect.top == self.rect.top and s.rect.bottom == self.rect.bottom) or (s.rect.bottom < self.rect.bottom and s.rect.bottom > self.rect.top) ):
				self.main.game = False

			if s.ver == 2 and ( (s.rect.bottom == self.rect.top) or (s.rect.top < self.rect.top and s.rect.bottom > self.rect.top) ) and ( (s.rect.left > self.rect.left and s.rect.left < self.rect.right) or (s.rect.left == self.rect.left and s.rect.right == self.rect.right) or (s.rect.left < self.rect.left and s.rect.right > self.rect.left) ):
				self.main.game = False

			if s.ver == 3 and ( (s.rect.right == self.rect.left) or (s.rect.left < self.rect.left and s.rect.left > self.rect.left) ) and ( (s.rect.bottom > self.rect.bottom and s.rect.top < self.rect.bottom) or (s.rect.top == self.rect.top and s.rect.bottom == self.rect.bottom) or (s.rect.bottom < self.rect.bottom and s.rect.bottom > self.rect.top) ):
				self.main.game = False

	def jump(self):
		if self.on_ground and self.last_jump == 0:
			self.on_ground = False
			self.vel.y = -11
			self.last_jump = 15

	def shoot(self):
		if self.weapon == 1:
			if self.last_shot == 0:
				self.last_shot = 60
				b = Bullet(self.last_direction, '0', self.rect.center, 'p')
				self.main.sprites.add(b)
				self.main.shots.add(b)
		elif self.weapon == 2:
			if self.last_shot == 0:
				self.last_shot = 60
				b1 = Bullet(self.last_direction, '0', self.rect.center, 'p')
				b2 = Bullet(self.last_direction, '1', self.rect.center, 'p')
				b3 = Bullet(self.last_direction, '2', self.rect.center, 'p')
				self.main.sprites.add(b1)
				self.main.sprites.add(b2)
				self.main.sprites.add(b3)
				self.main.shots.add(b1)
				self.main.shots.add(b2)
				self.main.shots.add(b3)