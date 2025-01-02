import pygame
from pygame.locals import *


class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y,SIZE_TILE):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('./images/monster.png')		
		# self.image = pygame.transform.scale(self.image, (46, 35))
		self.image = pygame.transform.scale(self.image, (int(SIZE_TILE-10), int(SIZE_TILE-10)))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y-10
		self.direction = 1
		self.delay_counter = 0

	def update(self):
		self.rect.x += self.direction
		self.delay_counter += 1
		if abs(self.delay_counter) > 25:
			self.direction *= -1
			self.delay_counter *= -1