
import pygame
from pygame.locals import *

class User():
    def __init__(self,screen,x,y,name,arrow_x,arrow_y):
        self.screen = screen
        self.name = name
        self.img = pygame.image.load('./images/dog.png')
        self.img = pygame.transform.scale(self.img , (50, 70))

        
        self.arrowimg = pygame.image.load('./images/arrow.png')
        self.arrowimg = pygame.transform.scale(self.arrowimg , (100, 70))

        
        self.arrow_rec = self.arrowimg.get_rect()
        self.arrow_rec.x = arrow_x
        self.arrow_rec.y = arrow_y


        self.rec = self.img.get_rect()
        self.rec.x = x 
        self.rec.y = y

    def setText(self):
        mFont = pygame.font.SysFont("arial", 30)
        mtext = mFont.render(f'{self.name}', True, 'black')
        tRec = mtext.get_rect()
        tRec.centerx = self.rec.x
        tRec.centery = self.rec.top-10
        self.screen.blit(mtext, tRec)

    def draw(self,x,y,name,arrows):      
        self.rec.x = x 
        self.rec.y = y
        self.name = name
        self.setText()
        self.screen.blit(self.img, self.rec)
        
        for arrow in arrows:
            self.arrow_rec.x= arrow[0]
            self.arrow_rec.y = arrow[1]
            self.screen.blit(self.arrowimg, self.arrow_rec)




