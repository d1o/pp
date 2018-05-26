from sets import *
from level import *
from camera import *
from playerclass import *
from blockclass import *
from bulletclass import *
from enemyclass import *
from pntclass import *
from bonusclass import *
import random

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

		pygame.font.init()
		self.font1 = pygame.font.Font('fonts/Ubuntu-R.ttf', 64)	
		self.font2 = pygame.font.Font('fonts/Ubuntu-R.ttf', 30)
		self.font3 = pygame.font.Font('fonts/Ubuntu-R.ttf', 20)
		
	def screen(self):
		self.screen_loop = True
		self.decision = 0

		pos1 = (WIDTH/20, 10*HEIGHT/20)
		self.txt_positions = [pos1, (pos1[0], pos1[1]+64), (pos1[0], pos1[1]+128), (pos1[0], pos1[1]+192)]
		self.pnt = Pnt()

		while self.screen_loop:
			if self.game == True:
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
							self.screen_loop = False

				self.pnt.rect.midright = pygame.math.Vector2(self.txt_positions[self.decision][0], self.txt_positions[self.decision][1]+36)

				self.WINDOW.fill(RED)
				self.WINDOW.blit(self.text_start,self.r_text_start)
				self.WINDOW.blit(self.text_instructions,self.r_text_instructions)
				self.WINDOW.blit(self.text_level,self.r_text_level)
				self.WINDOW.blit(self.text_exit,self.r_text_exit)
				self.WINDOW.blit(self.pnt.image,self.pnt.rect)
				pygame.display.flip()

			else:
				if self.lvl_won == True:
					for e in pygame.event.get():
						if e.type == QUIT:
							self.runnig = False
							sys.exit()

					k = pygame.key.get_pressed()
					if k[pygame.K_RETURN]: 
						
						self.decision = 0
						self.screen_loop = False

					self.text_game_over = self.font1.render('You beat the level!', 0, WHITE)
					self.text_press_ret = self.font2.render('Press return to start...', 0, WHITE)

					self.WINDOW.fill(GREEN)
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
						
						self.decision = 0
						self.screen_loop = False

					self.text_game_over = self.font1.render('GAME OVER', 0, WHITE)
					self.text_press_ret = self.font2.render('Press return to start...', 0, WHITE)

					self.WINDOW.fill(BLACK)
					self.WINDOW.blit(self.text_game_over,(13*WIDTH/40, HEIGHT/5))
					self.WINDOW.blit(self.text_press_ret,(WIDTH/22, 7*HEIGHT/8))
					pygame.display.flip()

		if self.decision == 0:
			self.start()
		else:
			self.runnig = False
			sys.exit()

	def start(self):
		self.score = 0
		self.sprites = pygame.sprite.Group()		#wszystkie sprity
		self.blocks = pygame.sprite.Group()			#sciany
		self.boxes = pygame.sprite.Group()			#skrzynki
		self.shots = pygame.sprite.Group()			#wystrzelone pociski
		self.bonuses = pygame.sprite.Group()		#bonusy z punktami
		self.weapons = pygame.sprite.Group()		#bonusy z bronia
		self.enemies = pygame.sprite.Group()		#przeciwnicy
		self.spikes = pygame.sprite.Group()		#kolce pionowo w gore

		self.player = Player(WIDTH/2, HEIGHT/2, self)
		self.sprites.add(self.player)

		self.lvl_won = False

		for b in BLOCKS:
			self.sprites.add(b)
			self.blocks.add(b)

		for bo in B:
			self.box = Box(bo[0], bo[1], self)
			self.sprites.add(self.box)
			self.boxes.add(self.box)

		for e in E:
			self.enemy = Enemy1(e[0], e[1], self)
			self.sprites.add(self.enemy)
			self.enemies.add(self.enemy)

		for s in S:
			self.spi = Spikes(s[0], s[1], 3, self)
			self.sprites.add(self.spi)
			self.spikes.add(self.spi)
			self.blocks.add(self.spi)

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
				if self.game: self.game = False
				self.running = False
				sys.exit()

	def update(self):
		self.sprites.update()
		self.player.update()
		self.camera.update(self.player)

		self.colls()

		
	def colls(self):
		######## CZY POCISK TRAFIŁ W ŚCIANĘ/KOLCE ########
		for b in self.blocks:
			shots_bricks_coll = pygame.sprite.spritecollide(b, self.shots, True)
		for s in self.spikes:
			shots_bricks_coll = pygame.sprite.spritecollide(s, self.shots, True)

		######## CZY POCISK TRAFIŁ W SKRZYNKĘ ########
		for bo in self.boxes:
			shots_box_coll = pygame.sprite.spritecollide(bo, self.shots, True)
			if shots_box_coll:
				if bo.shots < 2: bo.shots += random.randint(1,2)
				else: 
					self.bonus(bo.rect.center, 'box')
					bo.kill()

		######## CZY POCISK TRAFIŁ W PRZECIWNIKA ########
		for e in self.enemies:
			shots_enemies_colls = pygame.sprite.spritecollide(e, self.shots, True)
			if shots_enemies_colls:
				self.score += 50
				self.bonus(e.rect.center, 'enemy')
				e.kill()

		######## CZY PRZECIWNIK TRAFIŁ NA GRACZA ########
		player_enemies_colls = pygame.sprite.spritecollide(self.player, self.enemies, False)
		if player_enemies_colls:
			self.game = False

		######## CZY GRACZ WYPADŁ POZA MAPĘ ########
		if self.player.pos.y >= len(level) * TILESIZE + 5 * TILESIZE:
			self.game = False

		######## CZY GRACZ DOTARŁ DO KOŃCA MAPY ########
		if self.player.rect.right >= LVL_W * TILESIZE - 3 * TILESIZE:
			self.lvl_won = True
		if self.lvl_won:
			self.game = False

		######## CZY GRACZ PODNIÓSŁ BONUS/BRON ########
		bns_pla_coll = pygame.sprite.spritecollide(self.player, self.bonuses, True)
		for b in bns_pla_coll:
			self.score += b.pts

		wpn_pla_coll = pygame.sprite.spritecollide(self.player, self.weapons, True)
		for b in wpn_pla_coll:
			self.player.weapon = b.v

	def bonus(self, pos, who):
		bns = Bonus(pos, who)
		wpn = Weapon(pos, random.randint(1,2))
		if who == 'box':
			if random.randint(1,3) == 1:
				if random.randint(1,2) == 1:	#wybiera czy bonus punktowy czy bron
					self.sprites.add(bns)
					self.bonuses.add(bns)
				else:
					self.sprites.add(wpn)
					self.weapons.add(wpn)

		elif who == 'enemy':
			if random.randint(1,5) == 1:
				if random.randint(1,2) == 1:	#wybiera czy bonus punktowy czy bron
					self.sprites.add(bns)
					self.bonuses.add(bns)
				else:
					self.sprites.add(wpn)
					self.weapons.add(wpn)

	def draw(self):
		self.WINDOW.fill(WHITE)
		for s in self.sprites:
			self.WINDOW.blit(s.image, self.camera.move_obj(s))

		scr_str = str(self.score)
		while len(scr_str) != 5:
			scr_str = '0' + scr_str
		self.text_score = self.font3.render('score: '+scr_str, 0, BLACK)

		self.WINDOW.blit(self.text_score,(8.5*WIDTH/10, HEIGHT/50))
		pygame.display.flip()

g = Game()
while g.running:
	g.screen()

pygame.quit()