import pygame
from pygame.locals import *

class Exit(pygame.sprite.Sprite):
	def __init__(self, x, y,SIZE_TILE):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('./images/exit.png')
		self.image = pygame.transform.scale(img, (SIZE_TILE, int(SIZE_TILE*1.5)))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y-(SIZE_TILE)
