
import pygame
from pygame.locals import *
from client import *


class arrow():
    def __init__(self,screen,rec):#ret : 화살이 시작될 위치값
        self.screen = screen
        self.img = pygame.image.load('./images/arrow.png')
        self.img = pygame.transform.scale(self.img , (100, 50))

        #화살이 그려질 시작 위치 잡기
        self.rec = self.img.get_rect()
        self.rec.x = rec[0] 
        self.rec.y = rec[1]
        

    def draw(self):      
        if (self.rec.x) > 0:  
            self.rec.x -= 5
            self.screen.blit(self.img, self.rec)
            return False
        else:
            return True

