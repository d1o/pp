from sets import *
from bulletclass import *

class Player():
	def __init__(self, x):
		self.pimg = pygame.image.load('img/pla2.png')	

		self.pos_x = x
		self.pos_y = HEIGHT - self.pimg.get_height() - 40
		self.ground = HEIGHT - 40
		self.vel_x = 0
		self.vel_y = 0

		############ ZMIENNE ODPOWIEDZIALNE ZA SKAKANIE ############
		self.jumping = False
		self.wait_for_jump = 0

		############ ZMIENNE ODPOWIEDZIALNE ZA ANIMACJE POSTACI ############
		self.weapon = 2		#0-pisolet, 2-dwa pistolety, 4-shotgun, 6-ak
		self.row = 0
		self.col = 0

		############ POCISKI ############
		self.bullets = []
		self.shooted = 0
		self.dual_pistol_shooted = 0
		self.shotgun_shooted = 0
		self.rifle_shooted = 0


	def move(self, window):
		key = pygame.key.get_pressed()
		if key[pygame.K_LEFT] or key[pygame.K_a]:
			self.vel_x = -7
			self.row = self.weapon + 1		#obracanie postaci
			self.choose_img()

		if key[pygame.K_RIGHT] or key[pygame.K_d]: 
			self.vel_x = 7
			self.row = self.weapon			#obracanie postaci
			self.choose_img()

		if (key[pygame.K_w] or key[pygame.K_UP]) and not self.jumping and self.wait_for_jump == 0:
			self.jumping = True
			self.vel_y = 20
			self.wait_for_jump = 30

		if key[pygame.K_SPACE]:
			############ OGRANICZENIE STRZELANIA W CZASIE ############
			if self.weapon == 0 and self.shooted == 0:
				self.shooted = 25
				self.shoot()

			if self.weapon == 2 and self.shooted == 0:
				self.shooted = 25
				self.shoot()

			if self.weapon == 4 and self.shooted == 0:
				self.shooted = 25
				self.shoot()

			if self.weapon == 6 and self.shooted == 0:
				self.shooted = 15
				self.shoot()

		if key[pygame.K_1]:
			self.weapon = 0
		if key[pygame.K_2]:
			self.weapon = 2
		if key[pygame.K_3]:
			self.weapon = 4
		if key[pygame.K_4]:
			self.weapon = 6

		############ RUCH W POZIOMIE ###############
		self.pos_x += self.vel_x

		############ OGRANICZENIE SKOKOW W CZASIE ############
		if self.wait_for_jump > 0:
			self.wait_for_jump -= 1

		############ GDY GRACZ SKOCZYL ############
		if self.jumping and self.vel_y >= -20:
			self.pos_y -= self.vel_y
			self.vel_y -= 2
		else:
			self.pos_y = self.ground
			self.vel_y = 0
			self.jumping = False

		self.draw(window)

	def choose_img(self):
		############ ANIMACJA RUCHU ############
		if not self.jumping:
			if self.col < 5:
				self.col += 1
			else:
				self.col = 1

	def shoot(self):
		if self.shooted != 0:
			self.bullets.append(PBullet(self.pos_x, self.pos_y, self.row))

	def draw(self, window):
		if self.vel_x == 0:	#gdy gracz stoi w miejscu
			self.col = 0

		window.blit(self.pimg, (self.pos_x, self.pos_y-18), (0+50*self.col, 0+50*self.row, 50, 50))
		self.vel_x = 0

		if len(self.bullets) != 0:
			for i in range(len(self.bullets)): 
				self.bullets[i].draw(window)
				if self.bullets[i].pos_x < 0 or self.bullets[i].pos_x > WIDTH:
					self.bullets[i].pos_x = 2 * WIDTH
					self.bullets[i].pos_y = 2 * HEIGHT
					self.bullets[i].vel_x = 0

		if self.shooted != 0:
			self.shooted -= 1
