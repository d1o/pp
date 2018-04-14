from sets import *
from pclass import *
from blockclass import *
from level import *
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
		self.shots = pygame.sprite.Group()
		self.player = Player(416, 128, self)
		self.sprites.add(self.player)
		self.to_del = []

		for b in BLOCKS:
			self.sprites.add(b)

		for e in ENEMIES:
			self.sprites.add(e)

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
		if self.player.shooting:
			s = SingleBullet(self.player.last_dir, self.player.rect.center)
			self.sprites.add(s)
			self.shots.add(s)
			self.player.shooting = False
			self.player.wait_for_shoot = 60

		self.camera_move()
		self.sprites.update()
		self.player.update()

		for b in BLOCKS:
			shots_coll_bricks = pygame.sprite.spritecollide(b, self.shots, True)
			if shots_coll_bricks:
				self.hit_wall_anim()

		for e in ENEMIES:
			shots_coll_enemies = pygame.sprite.spritecollide(e, self.shots, True)
			if shots_coll_bricks:
				self.hit_enemy_anim()
				self.to_del.append(e)

	def camera_move(self):
		pass
		
	def hit_wall_anim(self):
		pass

	def hit_enemy_anim(self):
		pass

	def draw(self):
		self.WINDOW.fill(WHITE)
		self.sprites.draw(self.WINDOW)
		#self.draw_grid()
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