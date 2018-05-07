from sets import *
from level import *
from camera import *
from playerclass import *
from blockclass import *
from bulletclass import *
from enemyclass import *

class Game():
	def __init__(self):
		pygame.init()
		pygame.mixer.init()
		self.WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
		pygame.display.set_caption(TITLE)
		self.clock = pygame.time.Clock()
		self.running = True

	def start(self):
		self.sprites = pygame.sprite.Group()
		self.blocks = pygame.sprite.Group()
		self.shots = pygame.sprite.Group()

		self.enemies = pygame.sprite.Group()
		self.spikes = pygame.sprite.Group()

		self.player = Player(WIDTH/2, HEIGHT/2, self)
		self.sprites.add(self.player)
		self.to_del = []

		for b in BLOCKS:
			self.sprites.add(b)
			self.blocks.add(b)

		for e in E:
			self.enemy = Enemy1(e[0], e[1], self)
			self.sprites.add(self.enemy)
			self.enemies.add(self.enemy)

		for s in S:
			self.spi = Spikes1(s[0], s[1], self)
			self.sprites.add(self.spi)
			self.spikes.add(self.spi)

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

		######## CZY POCISK TRAFIŁ W ŚCIANĘ/KOLCE ########
		for b in BLOCKS:
			shots_bricks_coll = pygame.sprite.spritecollide(b, self.shots, True)
			if shots_bricks_coll:
				self.hit_wall_anim()
		for s in self.spikes:
			shots_bricks_coll = pygame.sprite.spritecollide(s, self.shots, True)
			if shots_bricks_coll:
				self.hit_wall_anim()

		######## CZY POCISK TRAFIŁ W PRZECIWNIKA ########
		for e in self.enemies:
			shots_enemies_colls = pygame.sprite.spritecollide(e, self.shots, True)
			if shots_enemies_colls:
				self.hit_enemy_anim()
				e.kill()

		######## CZY PRZECIWNIK TRAFIŁ NA GRACZA ########
		player_enemies_colls = pygame.sprite.spritecollide(self.player, self.enemies, False)
		if player_enemies_colls:
			self.game = False

		######## CZY GRACZ WYPADŁ POZA MAPĘ ########
		if self.player.pos.y >= len(level) * TILESIZE + 5 * TILESIZE:
			self.game = False

	def camera_move(self):
		pass
		
	def hit_wall_anim(self):
		pass

	def hit_enemy_anim(self):
		pass

	def draw(self):
		self.WINDOW.fill(WHITE)
		#self.sprites.draw(self.WINDOW)
		for s in self.sprites:
			self.WINDOW.blit(s.image, self.camera.move_obj(s))
		pygame.display.flip()

	def draw_grid(self):
		for x in range(0, WIDTH, TILESIZE):
			pygame.draw.line(self.WINDOW, BLACK, (x, 0), (x, HEIGHT))
		for y in range(0, HEIGHT, TILESIZE):
			pygame.draw.line(self.WINDOW, BLACK, (0, y), (WIDTH, y))

	def starting_screen(self):
		pass

	def lose_screen(self):
		pass

g = Game()
while g.running:
	g.start()
	g.lose_screen()


pygame.quit()