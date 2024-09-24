
import pygame
from pygame import *
from client import *
from arrow import*
from pygame.locals import *

class player():
    def __init__(self,screen:Surface,x,y,name,client:socketClient):
        self.screen = screen
        self.name = name
        self.client = client
        self.img = pygame.image.load('./images/dog.png')
        self.img = pygame.transform.scale(self.img , (50, 70))
        self.img_r = pygame.transform.flip(self.img, False, False) #반전x,y
        self.img_l = pygame.transform.flip(self.img, True, False) #반전x,y


        
        self.explosion_img = pygame.image.load('./images/explosion.png')
        self.explosion_img = pygame.transform.scale(self.explosion_img , (50, 50))

        #player
        self.rec = self.img.get_rect() 
        self.rec.x = x 
        self.rec.y = y
        self.player_dir = -5 

        # arrow
        self.arrows = []
        self.arrows_position = []
        self.arrow_delay = 0
        self.arrow_once = 0
        self.arrow_dir = -5 
        self.arrow_lr = -5

        # hp
        self.hp = 10
        self.hp_once = 0

        # 기타
        self.explosion_delay = 0
        self.explosion_delay_1 = 0

    # 플레이어 움직임
        #1 = 중력 , 2 = 점프 ,  
        self.player_state = 0
        # 점프 
        self.jump = 20
        self.jump_state = 0
        self.jump_delay = 0

        # 중력 
        self.gravity = 1
        self.gravity_state = 0



    def player_motion(self):
        #내려오는 효과 
        if self.screen.get_height()+30 > self.rec.y and self.jump_state == 0:
            self.player_state = 1
        if self.player_state == 1:
            if self.screen.get_height()-80 > self.rec.y:
                self.gravity += 0.4     
                self.rec.y += self.gravity
            else:
                self.gravity = 1
                self.player_state = 0
            # 점프 
        if self.player_state == 2:
            if self.jump_state == 1:
                if self.jump > 0:
                    self.jump -= 2 
                    self.rec.y -= self.jump 
                elif self.jump <= 0:
                    self.jump = 20
                    self.jump_state = 0
                    self.player_state = 1
# 내려오고 올라가는 효과 
#      1 1
#     2   2
#    3     3
#   4       4
#  5         5
# 6           6

    def setText(self):        
        for arrow in self.client.arrows:
            arrow_rec = pygame.Rect(arrow[0],arrow[1],100,50)
            if arrow_rec.colliderect(self.rec):
                self.explosion_delay = pygame.time.get_ticks()
                if self.hp > 0:
                    self.hp -= 1
                    self.hp_once = 1
        if (pygame.time.get_ticks()) - self.explosion_delay < 500:
            self.screen.blit(self.explosion_img,(self.rec.x,self.rec.y))

                

        mFont = pygame.font.SysFont("arial", 30)
        mtext = mFont.render(f'{self.name}:{self.hp}', True, (17,103,225))
        tRec = mtext.get_rect()
        tRec.centerx = self.rec.x+27
        tRec.centery = self.rec.top-15
        self.screen.blit(mtext, tRec)

    def moving(self):
        key_pressed = pygame.key.get_pressed()
        is_press = False
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            is_press = True
            if self.rec.y < self.screen.get_height()-80:
                self.rec.y += 5
        if key_pressed[K_a] or key_pressed[K_LEFT]: #왼  
            self.img = self.img_l
            self.arrow_lr = -5

            self.player_dir = -5
            is_press = True
            self.rec.x -= 5
            if self.rec.x < 0:
                self.rec.x = 0
        if key_pressed[K_d] or key_pressed[K_RIGHT]: #오
            self.img = self.img_r
            self.arrow_lr = 5

            self.player_dir = 5
            is_press = True
            if self.rec.x < self.screen.get_width()-50: 
                self.rec.x += 5     
        if key_pressed[K_h]:
            self.arrow_dir = self.arrow_lr
            is_press = True
            if (pygame.time.get_ticks()) - self.arrow_delay > 100:
                self.arrow_delay = pygame.time.get_ticks() 
                x = self.rec.x
                y = self.rec.y
                ar = arrow(self.screen,(x,y),self.arrow_dir)
                self.arrows.append(ar)
        if key_pressed[K_SPACE] or key_pressed[K_w] or key_pressed[K_UP]:
            if (pygame.time.get_ticks()) - self.jump_delay > 500:
                self.jump_delay = pygame.time.get_ticks()
                self.jump_state = 1
                self.player_state = 2
        if key_pressed[K_l]:
            self.rec.y = 100

            


        return is_press
    
    def updateArrow(self,member):
        #화살 날아가는 장면 연출 
        self.use = member[0]
        self.arrows_position = []       
        for i, arrow in enumerate(self.arrows):    
            if self.use.name is not None:
                if self.use.rec.colliderect(arrow.rec):
                    self.explosion_delay_1 = pygame.time.get_ticks()
                    del self.arrows[i] #삭제
            if (pygame.time.get_ticks()) - self.explosion_delay_1 < 500:
                self.screen.blit(self.explosion_img,(self.use.rec.x,self.use.rec.y))
            if arrow.draw():  #이동하며 그린다. 
                del self.arrows[i] #삭제 
            else:
                self.arrows_position.append((arrow.rec.x,arrow.rec.y))

    def draw(self,member):     
        result = self.moving()
        self.player_motion()
        self.screen.blit(self.img, self.rec)
        self.setText()
        if result == True or len(self.arrows_position) > 0 or self.arrow_once or self.hp_once == 1 or self.player_state != 0:
            self.client.send_data(self.rec,self.name,self.hp,self.player_dir,self.arrow_dir,self.arrows_position)
            self.arrow_once = len(self.arrows_position)
            self.hp_once = 0
        self.updateArrow(member)
        return result



