
import pygame
from pygame.locals import *
from player import *
from client import *
from user import *
from arrow import *
import pyautogui
    
class game():
    def __init__(self) -> None:
        pygame.init() #pygame 초기화
        pygame.display.set_caption("codingnow.co.kr") #타이틀

        #기본 변수 생성 및 초기화
        self.isActive = True 
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 1000
        self.clock = pygame.time.Clock() #프레임을 처리 하기위해
        name = pyautogui.prompt('이름을 입력하세요','채팅입력')  
        self.rec_x = -1
        self.rec_y = -1
        #스크린 생성
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT)) #화면생성
        self.screen.get_width()
        self.screen.get_height()

        self.client = socketClient()
        self.me = player(self.screen,300,200,name,self.client)
        self.member = []
        user = User(self.screen,0,0,"",0,0)
        self.member.append(user)



#이벤트 확인 및 처리 함수
    def eventProcess(self):
        for event in pygame.event.get():#이벤트 가져오기
            if event.type == QUIT: #종료버튼?
                self.isActive = False
            if event.type == pygame.KEYDOWN:#키 눌림?
                if event.key == pygame.K_ESCAPE:#ESC 키?
                    self.isActive = False                 

    def game_run(self):#무한 반복 문

        while self.isActive:
            self.screen.fill((255, 255, 255)) #화면을 흰색으로 채우기
            self.eventProcess() #이벤트 함수 호출
    
            for user in self.member:
                if self.client.name != "":
                    user.draw(self.client.x,self.client.y,self.client.name,self.client.arrows)
        
            if self.me.draw():
                pass

            pygame.display.update() #화면 갱신
            self.clock.tick(60) #초당 60프레임 갱신을 위한 잠시 대기

game_m = game()
game_m.game_run()