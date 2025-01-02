import pygame
from pygame.locals import *

class Block(pygame.sprite.Sprite):
	def __init__(self, x, y,SIZE_TILE, file,move_x = 0, move_y = 0):
		pygame.sprite.Sprite.__init__(self)
		# img = pygame.image.load(f'./images/platform.png')
		img = pygame.image.load(f'./images/{file}.png')
		if move_x==0 and move_y==0:
			self.image = pygame.transform.scale(img, (SIZE_TILE, SIZE_TILE))
		else:
			self.image = pygame.transform.scale(img, (SIZE_TILE, int(SIZE_TILE / 2)))
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.delay_counter = 0
		self.direction = 1
		self.move_x = move_x
		self.move_y = move_y

	def update(self):
		self.rect.x += self.direction * self.move_x
		self.rect.y += self.direction * self.move_y
		self.delay_counter += 1
		if abs(self.delay_counter) > 50:
			self.direction *= -1
			self.delay_counter *= -1