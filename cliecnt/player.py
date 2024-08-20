
import pygame
from arrow import*
from pygame.locals import *

class player():
    def __init__(self,screen,x,y,name,client):
        self.screen = screen
        self.name = name
        self.client = client
        self.player_imgs = []
        for player_img in self.player_imgs:
            self.img = pygame.image.load('./images/dog.png')
            self.img = pygame.transform.scale(self.img , (50, 70))
            self.img_r = pygame.transform.flip(self.img, False, False) #반전x,y
            self.player_imgs.append(self.img_l)
            self.img_l = pygame.transform.flip(self.img, True, False) #반전x,y
            self.player_imgs.append(self.img_r)

        #화살이 그려질 시작 위치 잡기
        self.rec = self.img.get_rect()
        self.rec.x = x 
        self.rec.y = y

        self.arrows = []
        self.arrows_position = []
        self.arrow_delay = 0


    def setText(self):
        mFont = pygame.font.SysFont("arial", 40)
        mtext = mFont.render(f'{self.name}', True, 'black')
        tRec = mtext.get_rect()
        tRec.centerx = self.rec.x+27
        tRec.centery = self.rec.top-15
        self.screen.blit(mtext, tRec)

    def moving(self):
        key_pressed = pygame.key.get_pressed()
        is_press = False
        if key_pressed[K_w]:
            is_press = True
            self.rec.y -= 5
            if self.rec.y  < 0:
                self.rec.y = 0
        if key_pressed[K_s]:
            is_press = True
            if self.rec.y < self.screen.get_height()-80:
                self.rec.y += 5
        if key_pressed[K_a]:
            is_press = True
            self.rec.x -= 5
            if self.rec.x < 0:
                self.rec.x = 0
        if key_pressed[K_d]:
            is_press = True
            if self.rec.x < self.screen.get_width()-50: 
                self.rec.x += 5     
        if key_pressed[K_SPACE]:
            if (pygame.time.get_ticks()) - self.arrow_delay > 500:
                self.arrow_delay = pygame.time.get_ticks() 
                x = self.rec.x
                y = self.rec.y
                ar = arrow(self.screen,(x,y))
                self.arrows.append(ar)
        return is_press
    
    
    def updateArrow(self):
        #화살 날아가는 장면 연출 
        self.arrows_position = []       
        for i, arrow in enumerate(self.arrows):
            if arrow.draw():  #이동하며 그린다.  
                del self.arrows[i] #삭제
            else:
                self.arrows_position.append((arrow.rec.x,arrow.rec.y))
            
        # print(self.arrows_position)

    def draw(self):        
        result = self.moving()
        self.updateArrow()
        self.setText()
        self.screen.blit(self.img, self.rec)
        self.client.send_data(self.rec,self.name,self.arrows_position)
        return result



