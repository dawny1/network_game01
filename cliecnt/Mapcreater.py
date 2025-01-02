
import pygame
from pygame.locals import *

from map.map_data import *
from map.enemy import *
from map.lava import *
from map.block import *
from map.exit import *
from map.coin import *

class MapCreate():
    SIZE_TILE = 50
    
    def __init__(self,screen):
        self.screen = screen

        self.enemy_group = pygame.sprite.Group()
        self.lava_group = pygame.sprite.Group()
        self.block_group = pygame.sprite.Group()
        self.coin_group = pygame.sprite.Group()
        self.exit_group = pygame.sprite.Group()

        self.init_map()
        
    def init_map(self):   
        data = Map_data.data[0]
        self.enemy_group.empty()
        self.lava_group.empty()
        self.block_group.empty()
        self.coin_group.empty()
        self.exit_group.empty()
        
        for i, row in enumerate(data):
            for k,tile in enumerate(row):
                x = k * self.SIZE_TILE
                y = i * self.SIZE_TILE
        #         if tile == 0:#
        #             per = random.randint(0,100)
        #             if(per < 20):
        #                 self.coin_group.add(Coin(x, y,self.SIZE_TILE))
        #         if tile == 1:#흙
        #             self.block_group.add(Block(x, y,self.SIZE_TILE,'dirt', 0, 0))
        #         if tile == 2:#풀밭
        #             self.block_group.add(Block(x, y,self.SIZE_TILE,'grass', 0, 0))
        #         if tile == 3:#장애물
        #             self.enemy_group.add(Enemy(x, y,self.SIZE_TILE))
                # if tile == 4:#수평이동 바닥
                #     self.block_group.add(Block(x, y,self.SIZE_TILE,'platform', 1, 0))
                # if tile == 5:#수직이동 바닥
                #     self.block_group.add(Block(x, y,self.SIZE_TILE,'platform', 0, 1))
        #         if tile == 6:#용암
        #             self.lava_group.add(Lava(x, y,self.SIZE_TILE))
        #         if tile == 7:#점수
        #             self.coin_group.add(Coin(x, y,self.SIZE_TILE))
        #         if tile == 8:#완료
        #             self.exit_group.add(Exit(x,y,self.SIZE_TILE))   
        #                         
    def draw_block(self,blocks):
        self.block_group.empty()
        for block in blocks:
            self.block_group.add(Block(block[0], block[1],self.SIZE_TILE,'grass', 0, 0))


            
    def draw_grid(self):        
        lines = int(self.screen.get_width()/self.SIZE_TILE)
        size = self.SIZE_TILE
        width = self.screen.get_width()
        height = self.screen.get_height()
        color = (250, 250, 250)
        for line in range(lines):
            #가로줄
            pygame.draw.line(self.screen, color, (0, line * size), (width, line * size))
            #세로줄
            pygame.draw.line(self.screen, color, (line * size, 0), (line * size, height))

    def draw(self):     

        # self.draw_grid()

        self.block_group.update()
        self.block_group.draw(self.screen)
        
        #나머지를 넣어 봅니다.        
        self.lava_group.update()    
        self.lava_group.draw(self.screen)  
        self.enemy_group.update() 
        self.enemy_group.draw(self.screen) 
        # self.coin_group.update()    
        # self.coin_group.draw(self.screen)  
        # self.exit_group.update() 
        self.exit_group.draw(self.screen) 