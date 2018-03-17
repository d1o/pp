from sets import *
from playerclass import *
from pisbulclass import *

class Game():
	def __init__(self):
		pygame.init()
		self.running = True
		self.window = pygame.display.set_mode((WIDTH, HEIGHT))
		self.window.fill(WHITE)
		self.fpsclock = pygame.time.Clock()
		pygame.display.set_caption(title)

	def start(self, player):
		self.loop(player)

	def loop(self, player):
		self.playing = True
		while self.playing:
			self.window.fill(WHITE)
			player.move(self.window)
			self.events()
			self.update()
			self.fpsclock.tick(FPS)
			
	def events(self):
		for event in pygame.event.get():
			if event.type == QUIT:
				self.running = False
				if self.playing: self.playing = False
				pygame.quit()
				sys.exit()

	def update(self):
		pygame.display.update()

player = Player(200)
g = Game()
while g.running:
	g.start(player)