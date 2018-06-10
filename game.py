from load import *

class Game():
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True
		self.game = True

		self.lvl_won = False
		self.score = 0
		self.level = 1

		self.key_img = pygame.image.load('img/oth/key.png')

		pygame.font.init()
		self.font1 = pygame.font.Font('fonts/Ubuntu-R.ttf', 64)	
		self.font2 = pygame.font.Font('fonts/Ubuntu-R.ttf', 30)
		self.font3 = pygame.font.Font('fonts/Ubuntu-R.ttf', 20)
		self.font4 = pygame.font.Font('fonts/Ubuntu-R.ttf', 10)
		
	def screen(self):
		self.screen_loop = True
		self.decision = 0
		self.screen_n = 0

		pos1 = (WIDTH/20, 10*HEIGHT/20)
		self.txt_positions = [pos1, (pos1[0], pos1[1]+64), (pos1[0], pos1[1]+128), (pos1[0], pos1[1]+192)]
		self.pnt = Pnt()

		while self.screen_loop:
			if self.game == True:
				if self.screen_n == 0:
					for e in pygame.event.get():
						if e.type == QUIT:
							self.runnig = False
							sys.exit()
						if e.type == pygame.KEYDOWN:
							if e.key == pygame.K_DOWN:
								if self.decision < 3: self.decision += 1
							if e.key == pygame.K_UP:
								if self.decision > 0: self.decision -= 1
							if e.key == pygame.K_RETURN:
								if self.decision == 0:
									self.start()
								elif self.decision > 0 and self.decision < 3:
									self.screen_n = self.decision
									self.decision = 0
								else:
									self.screen_loop = False
									self.runnig = False
									sys.exit()

					self.text_start = self.font1.render('START', 0, WHITE)
					self.r_text_start = self.text_start.get_rect()
					self.r_text_start.topleft = pygame.math.Vector2(self.txt_positions[0])

					self.text_level = self.font1.render('LEVEL SELECT', 0, WHITE)
					self.r_text_level = self.text_level.get_rect()
					self.r_text_level.topleft = pygame.math.Vector2(self.txt_positions[1])

					self.text_instructions = self.font1.render('INSCTRUCTIONS', 0, WHITE)
					self.r_text_instructions = self.text_instructions.get_rect()
					self.r_text_instructions.topleft = pygame.math.Vector2(self.txt_positions[2])

					self.text_exit = self.font1.render('EXIT', 0, WHITE)
					self.r_text_exit = self.text_exit.get_rect()
					self.r_text_exit.topleft = pygame.math.Vector2(self.txt_positions[3])

					self.pnt.rect.midright = pygame.math.Vector2(self.txt_positions[self.decision][0], self.txt_positions[self.decision][1]+36)

					self.WINDOW.fill((0,4,30))
					self.WINDOW.blit(self.text_start,self.r_text_start)
					self.WINDOW.blit(self.text_instructions,self.r_text_instructions)
					self.WINDOW.blit(self.text_level,self.r_text_level)
					self.WINDOW.blit(self.text_exit,self.r_text_exit)
					self.WINDOW.blit(self.pnt.image,self.pnt.rect)
					pygame.display.flip()

					
				elif self.screen_n == 1:
					for e in pygame.event.get():
						if e.type == QUIT:
							self.runnig = False
							sys.exit()
						if e.type == pygame.KEYDOWN:
							if e.key == pygame.K_DOWN:
								if self.decision < 1: self.decision += 1
							if e.key == pygame.K_UP:
								if self.decision > 0: self.decision -= 1
							if e.key == pygame.K_RETURN:
								if self.decision == 0:
									self.level = 1
								if self.decision == 1:
									self.level = 2
								self.decision = 0
								self.screen_n = 0

					self.text_lvl01 = self.font1.render('LEVEL 01', 0, WHITE)
					self.r_text_lvl01 = self.text_start.get_rect()
					self.r_text_lvl01.topleft = pygame.math.Vector2(self.txt_positions[0])

					self.text_lvl02 = self.font1.render('LEVEL 02', 0, WHITE)
					self.r_text_lvl02 = self.text_level.get_rect()
					self.r_text_lvl02.topleft = pygame.math.Vector2(self.txt_positions[1])

					self.pnt.rect.midright = pygame.math.Vector2(self.txt_positions[self.decision][0], self.txt_positions[self.decision][1]+36)

					self.WINDOW.fill((0,4,30))
					self.WINDOW.blit(self.text_lvl01,self.r_text_lvl01)
					self.WINDOW.blit(self.text_lvl02,self.r_text_lvl02)
					self.WINDOW.blit(self.pnt.image,self.pnt.rect)
					pygame.display.flip()


				elif self.screen_n == 2:
					for e in pygame.event.get():
						if e.type == QUIT:
							self.runnig = False
							sys.exit()
						if e.type == pygame.KEYDOWN:
							if e.key == pygame.K_RETURN or e.key == pygame.K_ESCAPE:
								self.screen_n = 0

					self.text_1 = self.font2.render('Use AD or left and right arrow to move.', 0, WHITE)
					self.r_text_1 = self.text_start.get_rect()
					self.r_text_1.topleft = pygame.math.Vector2((10,10))

					self.text_2 = self.font2.render('Press W or up arrow to jump.', 0, WHITE)
					self.r_text_2 = self.text_start.get_rect()
					self.r_text_2.topleft = pygame.math.Vector2((10,70))

					self.text_3 = self.font2.render('Find key to open the door.', 0, WHITE)
					self.r_text_3 = self.text_start.get_rect()
					self.r_text_3.topleft = pygame.math.Vector2((10,130))

					self.text_4 = self.font2.render('Press F to use the key.', 0, WHITE)
					self.r_text_4 = self.text_start.get_rect()
					self.r_text_4.topleft = pygame.math.Vector2((10,190))

					self.WINDOW.fill((0,4,30))
					self.WINDOW.blit(self.text_1,self.r_text_1)
					self.WINDOW.blit(self.text_2,self.r_text_2)
					self.WINDOW.blit(self.text_3,self.r_text_3)
					self.WINDOW.blit(self.text_4,self.r_text_4)
					pygame.display.flip()


			else:
				if self.lvl_won == True:
					for e in pygame.event.get():
						if e.type == QUIT:
							self.runnig = False
							sys.exit()

					k = pygame.key.get_pressed()
					if k[pygame.K_RETURN]:
						self.start()
					if k[pygame.K_ESCAPE]:
						self.game = True

					self.text_game_over = self.font1.render('You beat the level!', 0, WHITE)
					self.text_press_ret = self.font2.render('Press return to start...', 0, WHITE)

					self.WINDOW.fill((51,127,57))
					self.WINDOW.blit(self.text_game_over,(13*WIDTH/40, HEIGHT/5))
					self.WINDOW.blit(self.text_press_ret,(WIDTH/22, 7*HEIGHT/8))
					pygame.display.flip()

				else:
					for e in pygame.event.get():
						if e.type == QUIT:
							self.runnig = False
							sys.exit()

					k = pygame.key.get_pressed()
					if k[pygame.K_RETURN]: 
						self.start()
					if k[pygame.K_ESCAPE]:
						self.game = True

					self.text_game_over = self.font1.render('GAME OVER', 0, WHITE)
					self.text_press_ret = self.font2.render('Press return to start...', 0, WHITE)

					self.WINDOW.fill((158, 28, 28))
					self.WINDOW.blit(self.text_game_over,(13*WIDTH/40, HEIGHT/5))
					self.WINDOW.blit(self.text_press_ret,(WIDTH/22, 7*HEIGHT/8))
					pygame.display.flip()

	def start(self):
		(self.LVL, self.LVL_H, self.LVL_W, self.bg) = level(self.level)

		self.score = 0
		self.sprites = pygame.sprite.Group()		#wszystkie sprity
		self.blocks = pygame.sprite.Group()			#sciany
		self.boxes = pygame.sprite.Group()			#skrzynki
		self.shots = pygame.sprite.Group()			#wystrzelone pociski
		self.bonuses = pygame.sprite.Group()		#bonusy z punktami
		self.weapons = pygame.sprite.Group()		#bonusy z bronia
		self.enemies = pygame.sprite.Group()		#przeciwnicy
		self.spikes = pygame.sprite.Group()			#kolce
		self.turrets = pygame.sprite.Group()		#wiezyczki
		self.platforms = pygame.sprite.Group()		#platformy
		self.ladders = pygame.sprite.Group()		#drabiny
		self.jumps = pygame.sprite.Group()			#jumppady
		self.doors = pygame.sprite.Group()			#drzwi
		self.keys = pygame.sprite.Group()			#klucze

		self.cls = pygame.sprite.Group()			#sprite, z ktorymi gracz i przeciwnicy moga kolidowac

		self.lvl_won = False

		COLLS = ['D1', 'D2', 'D3', 'D4', 'B0', 'B1', 'B2', 'WO', 'JU']
		PLATFORMS = ['DP', 'BP', 'WP']
		DESTRO = ['BO']
		NO_COLLS = ['BG']
		ENEMS = ['EE','S0','S1','S2','S3','TT', 'T0', 'T1']

		for i in range(len(self.LVL)):
			for j in range(len(self.LVL[i])):
				if self.LVL[i][j] == 'P0':
					self.player = Player(16+j*TILESIZE, 16+i*TILESIZE, self)
					self.sprites.add(self.player)

				if self.LVL[i][j] in COLLS:
					b = Block(16+j*TILESIZE, 16+i*TILESIZE, self.LVL[i][j])
					self.sprites.add(b)
					self.blocks.add(b)
					self.cls.add(b)
					if self.LVL[i][j] == 'JU':
						self.jumps.add(b)

				elif self.LVL[i][j][0] == 'C' and  self.LVL[i][j][1].isdigit():
					c = Coin(16+j*TILESIZE, 16+i*TILESIZE, self.LVL[i][j])
					self.sprites.add(c)
					self.bonuses.add(c)

				elif self.LVL[i][j][0] == 'Q' and  self.LVL[i][j][1].isdigit():
					b = Box(16+j*TILESIZE, 16+i*TILESIZE, self.LVL[i][j][1], self)
					self.sprites.add(b)
					self.boxes.add(b)
					self.cls.add(b)

				elif self.LVL[i][j] == 'KY':
					k = Key(16+j*TILESIZE, 16+i*TILESIZE)
					self.sprites.add(k)
					self.keys.add(k)

				elif self.LVL[i][j] == 'DD':
					d = Doors(j*TILESIZE, i*TILESIZE, self)
					self.sprites.add(d)
					self.doors.add(d)
					self.cls.add(d)

				elif self.LVL[i][j] in ENEMS:
					if self.LVL[i][j] == 'EE':
						e = Enemy1(16+j*TILESIZE, 16+i*TILESIZE, self)
						self.sprites.add(e)
						self.enemies.add(e)
					if self.LVL[i][j][0] == 'S':
						s = Spikes(16+j*TILESIZE, 16+i*TILESIZE, int(self.LVL[i][j][1]), self)
						self.sprites.add(s)
						self.spikes.add(s)
						self.blocks.add(s)
					if self.LVL[i][j] == 'TT':
						t = Turret(16+j*TILESIZE, 16+i*TILESIZE, self)
						self.sprites.add(t)
						self.turrets.add(t)
						self.cls.add(t)
					if self.LVL[i][j][0] == 'T' and  self.LVL[i][j][1].isdigit():
						t = Turret2(16+j*TILESIZE, 16+i*TILESIZE, self.LVL[i][j][1], self)
						self.sprites.add(t)
						self.turrets.add(t)
						self.cls.add(t)

				elif self.LVL[i][j] in PLATFORMS:
					p = Platform(16+j*TILESIZE, 16+i*TILESIZE, self.LVL[i][j], self)
					self.sprites.add(p)
					self.platforms.add(p)
					self.cls.add(p)
		
		self.camera = Camera()
		self.loop()

	def loop(self):
		self.game = True
		while self.game:
			self.clock.tick(FPS)
			self.events()
			self.update()
			self.draw()

	def events(self):
		for e in pygame.event.get():
			if e.type == QUIT:
				self.running = False
				sys.exit()

	def update(self):
		self.sprites.update()
		self.player.update()
		self.camera.update(self.player)
		self.colls()
		
	def colls(self):
		######## CZY POCISK TRAFIŁ W ŚCIANĘ/KOLCE/DRZWI ########
		pygame.sprite.groupcollide(self.blocks, self.shots, False, True)
		pygame.sprite.groupcollide(self.platforms, self.shots, False, True)
		pygame.sprite.groupcollide(self.spikes, self.shots, False, True)
		pygame.sprite.groupcollide(self.doors, self.shots, False, True)

		######## CZY POCISK TRAFIŁ W SKRZYNKĘ ########
		for bo in self.boxes:
			shots_box_coll = pygame.sprite.spritecollide(bo, self.shots, True)
			#if shots_box_coll:
			for s in shots_box_coll:
				if s.who == 'p':
					if bo.shots < 2: bo.shots += random.randint(1,2)
					else: 
						if bo.mode == 1:
							c = Coin(bo.pos.x, bo.pos.y, 'C1')
							self.sprites.add(c)
							self.bonuses.add(c)
						elif bo.mode == 2:
							wpn = Weapon(bo.pos, 1)
							self.sprites.add(wpn)
							self.weapons.add(wpn)
						elif bo.mode == 3:
							wpn = Weapon(bo.pos, 2)
							self.sprites.add(wpn)
							self.weapons.add(wpn)
						elif bo.mode == 4:
							bns = Bonus(bo.pos)
							self.sprites.add(bns)
							self.bonuses.add(bns)
						bo.kill()

		######## CZY POCISK TRAFIŁ W PRZECIWNIKA ########
		for e in self.enemies:
			shots_enemies_colls = pygame.sprite.spritecollide(e, self.shots, False)
			for s in shots_enemies_colls:
				if s.who == 'p':
					s.kill()
					self.score += 50
					e.kill()

		######## CZY POCISK TRAFIŁ W WIEŻYCZKĘ ########
		for t in self.turrets:
			shots_turrets_colls = pygame.sprite.spritecollide(t, self.shots, False)
			#if shots_enemies_colls:
			for s in shots_turrets_colls:
				if s.who == 'p':
					s.kill()
					if t.lives > 0: t.lives -= 1
					else:
						self.score += 75
						t.kill()

		######## CZY GRACZ ZOSTAŁ TRAFIONY PRZEZ PRZECIWNIKA ########
		shots_playernemies_colls = pygame.sprite.spritecollide(self.player, self.shots, False)
		for s in shots_playernemies_colls:
			if s.who != 'p':
				self.game = False

		######## CZY PRZECIWNIK TRAFIŁ NA GRACZA ########
		player_enemies_colls = pygame.sprite.spritecollide(self.player, self.enemies, False)
		if player_enemies_colls:
			self.game = False

		######## CZY GRACZ WYPADŁ POZA MAPĘ ########
		if self.player.pos.y >= self.LVL_H * TILESIZE + 5 * TILESIZE:
			self.game = False

		######## CZY GRACZ DOTARŁ DO KOŃCA MAPY ########
		if self.player.rect.right >= self.LVL_W * TILESIZE - 3 * TILESIZE and self.player.on_ground:
			self.lvl_won = True
			if self.level == 1:
				self.level = 2
			else:
				self.level = 1
			self.game = False

		######## CZY GRACZ PODNIÓSŁ BONUS/MONETE/BRON/KLUCZ ########
		bns_pla_coll = pygame.sprite.spritecollide(self.player, self.bonuses, True)
		for b in bns_pla_coll:
			self.score += b.pts

		key_pla_coll = pygame.sprite.spritecollide(self.player, self.keys, True)
		for b in key_pla_coll:
			self.player.keys += 1

		wpn_pla_coll = pygame.sprite.spritecollide(self.player, self.weapons, True)
		for b in wpn_pla_coll:
			self.player.weapon = b.v

	def open_doors(self):
		doorsnum = len(self.doors)
		for d in self.doors:
			d.kill()
		if len(self.doors) < doorsnum:
			self.player.keys -= 1

	def draw(self):
		self.WINDOW.fill(SKY)
		self.WINDOW.blit(self.bg.image, self.camera.move_obj(self.bg))

		for s in self.sprites:
			self.WINDOW.blit(s.image, self.camera.move_obj(s))

		scr_str = str(self.score)
		while len(scr_str) != 5:
			scr_str = '0' + scr_str
		self.text_score = self.font3.render('score: '+scr_str, 0, BLACK)

		self.WINDOW.blit(self.text_score,(8.5*WIDTH/10, HEIGHT/50))
		if self.player.keys > 0:
			self.WINDOW.blit(self.key_img,(9.5*WIDTH/10, 4*HEIGHT/50))

		for d in self.doors:
			if math.fabs(self.player.pos.x - d.pos.x) <= 3 * TILESIZE and math.fabs(self.player.pos.y - d.pos.y) <= 3 * TILESIZE:
				if self.player.keys > 0:
					self.text_key_info = self.font4.render('PRESS F TO OPEN DOORS', 0, BLACK)
				else:
					self.text_key_info = self.font4.render('YOU NEED A KEY', 0, BLACK)
				self.WINDOW.blit(self.text_key_info,(WIDTH/2, HEIGHT - TILESIZE))

		pygame.display.flip()

g = Game()
while g.running:
	g.screen()

pygame.quit()