
import pygame
from pygame import *
from client import *
from arrow import *
from pygame.locals import *

class player():
    JUMP = 15
    jumped = False
    jump_y = 0
    game_mode = 0
    game_mode_once = 0
    addr = None

    def __init__(self,screen:Surface,x,y,name,client:socketClient,map):
        self.screen = screen
        self.name = name
        self.client = client
        self.g_map = map
        self.img = pygame.image.load('./images/dog.png')
        self.img = pygame.transform.scale(self.img , (50, 70))
        self.img_r = pygame.transform.flip(self.img, False, False) #반전x,y
        self.img_l = pygame.transform.flip(self.img, True, False) #반전x,y

        self.explosion_img = pygame.image.load('./images/explosion.png')
        self.explosion_img = pygame.transform.scale(self.explosion_img , (50, 50))

        self.grass_img = pygame.image.load('./images/grass.png')
        self.grass_img = pygame.transform.scale(self.grass_img , (50, 50))
        
        #player
        self.rec = self.img.get_rect() 
        self.rec.x = x 
        self.rec.y = y

        self.rec_pre = self.rec.copy()

        self.player_dir = -5 

        self.arrows = []
        self.arrows_position = []
        self.arrow_delay = 0
        self.arrow_once = 0
        self.arrow_dir = -5 
        self.arrow_lr = -5
        self.arrow_del = 0

        # hp
        self.hp = 10
        self.hp_once = 0

        # 기타
        self.explosion_delay = 0
        self.explosion_delay_1 = 0


        # 블럭 
        self.block_up = 0

    def player_motion(self):
        dy = 0
        self.jump_y += 1
        if self.jump_y > self.JUMP:
            self.jump_y = self.JUMP
            if self.rec.bottom >= self.screen.get_height():
                self.jumped = False
        dy = self.jump_y
        return dy


    def check_colliderect_blocks(self):      
        dx = self.rec.x-self.rec_pre.x
        dy = self.rec.y-self.rec_pre.y

        self.rec = self.rec_pre.copy()

        xc = pygame.Rect(self.rec.x+dx, self.rec.y, self.rec.width, self.rec.height)#앞으로
        yc = pygame.Rect(self.rec.x, self.rec.y+dy, self.rec.width, self.rec.height)#위로

        # xc,yc는 플레이어 좌표,이미지크기
        for block in self.g_map.block_group:
            
            is_up = False
            is_down = False

            if block.rect.bottom > self.rec.bottom:#블럭위
                is_up = True

            if block.rect.top <= self.rec.top:#블럭아래
                is_down = True


            if block.rect.colliderect(yc):
                if is_up:
                    self.jumped = False
                    self.block_up = 1
                    dy = 0
                    self.rec.bottom = block.rect.top
                    if block.move_x != 0:
                        self.rec.x += block.direction * block.move_x
                if is_down:
                    dy = 0
                    if self.jumped and self.jump_y < 0:
                        self.jump_y *= -1
                    self.rec.top = block.rect.bottom
            else:
                if self.rec.bottom != block.rect.top:
                    self.block_up = 0

            if block.rect.colliderect(xc):
                dx = 0
            
                
        self.rec.y += dy
        self.rec.x += dx
        
        for arrow in self.client.arrows:
            arrow_rec = pygame.Rect(arrow[0],arrow[1],100,50)
            if arrow_rec.colliderect(self.rec):
                self.explosion_delay = pygame.time.get_ticks()
                if self.hp > 0:
                    self.hp -= 1
                    self.hp_once = 1
        if (pygame.time.get_ticks()) - self.explosion_delay < 500:
            self.screen.blit(self.explosion_img,(self.rec.x,self.rec.y))
                

        


    def setText(self):   
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
        # 
        if key_pressed[K_l]:
            self.rec.y = 100
        
        if key_pressed[K_SPACE] or key_pressed[K_w] or key_pressed[K_UP]:
            if self.jumped == False:
                self.jump_y = self.JUMP * (-1)
                self.jumped = True


            


        return is_press
    
    def updateArrow(self,member):
        #화살 날아가는 장면 연출 
        self.use = member[0]
        self.arrows_position = []       
        for i, arrow in enumerate(self.arrows):                
          
            if self.use.name is not None:
                if self.use.rec.colliderect(arrow.rect):
                    self.explosion_delay_1 = pygame.time.get_ticks()
                    del self.arrows[i] #삭제
            if (pygame.time.get_ticks()) - self.explosion_delay_1 < 500:
                self.screen.blit(self.explosion_img,(self.use.rec.x,self.use.rec.y))
            if pygame.sprite.spritecollide(arrow,self.g_map.block_group,False):
                del self.arrows[i] #삭제 
                
            if self.arrow_del == 1:
                del self.arrows[i]
            if arrow.draw():  #이동하며 그린다. 
                del self.arrows[i] #삭제 
            else:
                self.arrows_position.append((arrow.rect.x,arrow.rect.y))




    def draw(self,member):    
        self.updateArrow(member) 
        result = self.moving()
        # print(self.addr)
        dy = self.player_motion()
        self.rec.y+= dy
        

        self.check_colliderect_blocks()

        if self.rec.bottom > self.screen.get_height():
           self.rec.bottom = self.screen.get_height() 
           self.jumped = False
        self.screen.blit(self.img, self.rec)
        self.setText()      
        if self.game_mode_once == 0:
            self.game_mode = 1                                                                                                                                    #하는중
        if result == True or len(self.arrows_position) > 0 or self.arrow_once or self.hp_once == 1 or (self.rec.x != self.rec_pre.x) or (self.rec.y != self.rec_pre.y) or self.game_mode == 1:
            self.client.send_data(self.rec,self.name,self.hp,self.player_dir,self.arrow_dir,self.arrows_position)
            self.arrow_once = len(self.arrows_position)
            self.hp_once = 0
            # 하는중
            self.game_mode = 0
            self.game_mode_once = 1

            
        self.rec_pre = self.rec.copy()
        return result



