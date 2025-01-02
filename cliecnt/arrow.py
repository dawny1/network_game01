
import pygame
from pygame.locals import *
from client import *


class arrow():
    def __init__(self,screen,rec,arrow_dir):#ret : 화살이 시작될 위치값
        self.screen = screen
        self.arrow_dir = arrow_dir
        self.img = pygame.image.load('./images/arrow.png')
        self.img = pygame.transform.scale(self.img , (100, 50))
        if self.arrow_dir > 0:
            self.img = pygame.transform.flip(self.img, True, False) #반전x,y

        #화살이 그려질 시작 위치 잡기
        self.rect = self.img.get_rect()
        self.rect.x = rec[0] 
        self.rect.y = rec[1]
        

    def draw(self):  
        if (self.rect.x) > 0 and self.rect.x < self.screen.get_width():  
            self.rect.x += self.arrow_dir
            self.screen.blit(self.img, self.rect)
            return False
        else:
            return True

