
import pygame
from pygame.locals import *
from player import *
from client import *
from user import *
from arrow import *
from account import *
     
class game():
    def __init__(self) -> None:
        pygame.init() #pygame 초기화
        pygame.display.set_caption("codingnow.co.kr") #타이틀
        

        #기본 변수 생성 및 초기화
        self.isActive = True 
        self.SCREEN_WIDTH = 800
        self.SCREEN_HEIGHT = 800

        self.clock = pygame.time.Clock() #프레임을 처리 하기위해
        self.rec_x = -1
        self.rec_y = -1
        #스크린 생성
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT)) #화면생성
        self.screen.get_width()
        self.screen.get_height()
        self.bg_img = pygame.image.load('./images/bg.png')
        self.bg_img = pygame.transform.scale(self.bg_img,(self.SCREEN_HEIGHT,self.SCREEN_WIDTH))
        self.game_state = 0
        # game_state = 0은 시작화면  1 = 게임 2 = 게임 오버 

        self.client = socketClient()    

        self.acc = Account(self.screen)
        self.name = self.acc.run()
        # print(self.client.start_x)
        # print(self.client.start_y)
        self.me = player(self.screen,self.client.start_x,self.client.start_y,self.name,self.client)

        # 300 ,200 생성 좌표 
        self.member = []
        user = User(self.screen,0,0,"",100,0,0,0,0)
        self.member.append(user)

        self.jump = 0
        self.win = ""

#이벤트 확인 및 처리 함수
    def eventProcess(self):
        for event in pygame.event.get():#이벤트 가져오기
            # print(event)
            if event.type == QUIT: #종료버튼?
                self.isActive = False
            if event.type == pygame.KEYDOWN:#키 눌림?
                if event.key == pygame.K_ESCAPE:#ESC 키?
                    self.isActive = False
                if event.key == pygame.K_BACKSPACE: 
                    self.name = ""
                # if self.game_state == 2 and event.key == pygame.K_SPACE:
                #     self.game_state = 1
                #     self.me.hp = 10
                #     self.client.hp = 10
                    # 재시작
            if self.name is not None:
                self.game_state = 1
            if event.type == pygame.TEXTINPUT:
                if self.game_state == 0:
                    self.name += event.text
            if self.me.hp == 0 or self.client.hp == 0:
                self.game_state = 2


            self.client.game_state = self.game_state
            # self.me.player_jump = self.jump

    def input_name(self):
        mFont = pygame.font.SysFont("arial", 30)
        mtext = mFont.render(f'name:[{self.name}]', True,'black')
        tRec = mtext.get_rect()
        tRec.centerx = self.screen.get_width()/2
        tRec.centery = self.screen.get_height()/2-100
        self.screen.blit(mtext, tRec)
        
    def game_over(self):
        if self.me.hp < self.client.hp:
            self.win = self.client.name
        else:
            self.win = self.me.name
        mFont = pygame.font.SysFont("arial", 50)
        mtext = mFont.render(f"{self.win} win!!!", True,'red')
        tRec = mtext.get_rect()
        tRec.centerx = self.screen.get_width()/2
        tRec.centery = self.screen.get_height()/2-100
        self.screen.blit(mtext, tRec)

        # mFont = pygame.font.SysFont("arial", 50)
        # mtext = mFont.render(f'restart: space', True,'blue')
        # tRec = mtext.get_rect()
        # tRec.centerx = self.screen.get_width()/2
        # tRec.centery = self.screen.get_height()/2-50
        # self.screen.blit(mtext, tRec)
  
    def game_run(self):#무한 반복 문
        while self.isActive:
            self.screen.fill((255, 255, 255)) #화면을 흰색으로 채우기
            self.screen.blit(self.bg_img,(0,0))
            self.eventProcess() #이벤트 함수 호출

            if self.game_state == 0:#화면
                self.input_name()
            elif self.game_state == 1: #플레이
                self.me.draw(self.member)

                for user in self.member:
                    if self.client.name is not None:
                        user.draw(self.client.x,self.client.y,self.client.name,self.client.hp,self.client.player_dir,self.client.arrows)
            elif self.game_state == 2:
                self.game_over()
                #종료
            
            

            pygame.display.update() #화면 갱신
            self.clock.tick(60) #초당 60프레임 갱신을 위한 잠시 대기

game_m = game()
game_m.game_run()