import pygame
from pygame.locals import *

class Lava(pygame.sprite.Sprite):
	def __init__(self,x, y, SIZE_TILE):
		pygame.sprite.Sprite.__init__(self)
		img = pygame.image.load('./images/lava.png')
		self.image = pygame.transform.scale(img, (SIZE_TILE+1, int(SIZE_TILE / 2)))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y+(SIZE_TILE/2)
		self.direction = 1
		self.delay_counter = 0
	
	def update(self):
		self.delay_counter += 1
		if self.delay_counter > 5:
			self.direction *= -1
			self.delay_counter *= -1
			self.rect.x += self.direction