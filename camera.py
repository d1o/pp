from sets import *

class Camera():
	def __init__(self):
		self.width = WIDTH
		self.height = HEIGHT
		self.cam = pygame.Rect(0, 0, self.width, self.height)

	def move_obj(self, obj):
		return obj.rect.move(self.cam.topleft)

	def update(self, pla):
		self.pla_x = -pla.rect.x + int(WIDTH/2)
		self.pla_y = -pla.rect.y + int(HEIGHT/2)
		self.cam = pygame.Rect(self.pla_x, self.pla_y, self.width, self.height)