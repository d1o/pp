from sets import *
from pclass import *
from bclass import *
from level import *

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
		self.player = Player(64, 64)
		self.sprites.add(self.player)

		self.blocks = BLOCKS
		for b in self.blocks:
			self.sprites.add(b)

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
		colls = pygame.sprite.spritecollide(self.player, self.blocks, False)
		if colls:
			if self.player.vel.y > 0:
				self.player.pos.y = colls[0].rect.top + 1
			elif self.player.vel.y < 0:
				self.player.pos.y = colls[0].rect.bottom + TILESIZE -1
			elif self.player.vel.x > 0:
				self.player.rect.right = colls[0].rect.left
			elif self.player.vel.x < 0:
				self.player.rect.left = colls[0].rect.right
			self.player.vel.y = 0

		if self.player.rect.top <= HEIGHT/7:
			self.player.pos.y += abs(self.player.vel.y)
			for b in self.blocks:
				b.rect.y += abs(self.player.vel.y)
		elif self.player.rect.bottom >= 6*HEIGHT/7:
			self.player.pos.y -= abs(self.player.vel.y)
			for b in self.blocks:
				b.rect.y -= abs(self.player.vel.y)

	def draw(self):
		self.WINDOW.fill(WHITE)
		self.sprites.draw(self.WINDOW)
		pygame.display.flip()

	def starting_screen(self):
		pass

	def lose_screen(self):
		pass

g = Game()
while g.running:
	g.start()
	g.lose_screen()


pygame.quit()