import pygame
from pygame.locals import *
import random

class Coin(pygame.sprite.Sprite):
	def __init__(self, x, y,SIZE_TILE):
		pygame.sprite.Sprite.__init__(self)
		self.img = pygame.image.load('./images/coin.png')
		self.img = pygame.transform.scale(self.img, (int(SIZE_TILE / 2), int(SIZE_TILE / 2)))
		self.image = self.img
		self.rect = self.image.get_rect()
		self.rect.center = (x+(SIZE_TILE/2), y+(SIZE_TILE/2))
		self.delay_counter = 0
		self.angle = 0

	def update(self):
		self.delay_counter += 1
		if abs(self.delay_counter) > 5:
			self.delay_counter = 0
			self.angle = random.randint(0,360)
			self.image = pygame.transform.rotate(self.img, self.angle)