
import pygame
from pygame.locals import *

class User():
    def __init__(self,screen,x,y,name,arrow_x,arrow_y,arrow_dir):
        self.screen = screen
        self.name = name
        self.img = pygame.image.load('./images/dog.png')
        self.img = pygame.transform.scale(self.img , (50, 70))
        self.img_r = pygame.transform.flip(self.img, False, False) #반전x,y
        self.img_l = pygame.transform.flip(self.img, True, False) #반전x,y

        
        self.arrowimg = pygame.image.load('./images/arrow.png')
        self.arrowimg = pygame.transform.scale(self.arrowimg , (100, 50))
        self.arrowimg_r = pygame.transform.flip(self.arrowimg, False, False) #반전x,y
        self.arrowimg_l = pygame.transform.flip(self.arrowimg, True, False) #반전x,y


        self.arrow_rec = self.arrowimg.get_rect()
        self.arrow_rec.x = arrow_x
        self.arrow_rec.y = arrow_y
        self.arrow_dir = arrow_dir

        self.rec = self.img.get_rect()
        self.rec.x = x 
        self.rec.y = y

        print(self.arrow_dir)

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
        if self.arrow_dir == 5:
            self.img = self.img_r
        if self.arrow_dir == -5:
            self.img = self.img_l
        self.screen.blit(self.img, self.rec)
        for arrow in arrows:
            self.arrow_rec.x= arrow[0]
            self.arrow_rec.y = arrow[1]
            self.arrow_dir = arrow[2]
            if self.arrow_dir == 5:
                self.arrowimg = self.arrowimg_l
            elif self.arrow_dir == -5:
                self.arrowimg = self.arrowimg_r
            self.screen.blit(self.arrowimg, self.arrow_rec)




