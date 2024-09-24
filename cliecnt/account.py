

import pygame
from pygame import Surface
     
class Account():
    def __init__(self,screen:Surface) -> None:
        self.screen = screen
        self.bg_img = pygame.image.load('./images/bg.png')
        self.bg_img = pygame.transform.scale(self.bg_img,(self.screen.get_width(),self.screen.get_height()))
        self.isActive = True

        self.clock = pygame.time.Clock() #프레임을 처리 하기위해
        self.name = ""

#이벤트 확인 및 처리 함수
    def eventProcess(self):
        for event in pygame.event.get():#이벤트 가져오기
            if event.type == pygame.QUIT: #종료버튼?
                self.isActive = False
            if event.type == pygame.KEYDOWN:#키 눌림?
                if event.key == pygame.K_ESCAPE:#ESC 키?
                    self.isActive = False
                if event.key == pygame.K_BACKSPACE:  
                    self.name = ""
                if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:    
                    self.name = self.name   
                    self.isActive = False
            if event.type == pygame.TEXTINPUT:
                self.name += event.text

    def input_name(self):
        mFont = pygame.font.SysFont("arial", 30)
        mtext = mFont.render(f'name:[{self.name}]', True,'black')
        tRec = mtext.get_rect()
        tRec.centerx = self.screen.get_width()/2
        tRec.centery = self.screen.get_height()/2-100
        self.screen.blit(mtext, tRec)


    def run(self):#무한 반복 문
        while self.isActive:
            self.screen.fill((255, 255, 255)) #화면을 흰색으로 채우기
            self.screen.blit(self.bg_img,(0,0))
            self.eventProcess() #이벤트 함수 호출
            self.input_name()

            pygame.display.update() #화면 갱신
            self.clock.tick(60) #초당 60프레임 갱신을 위한 잠시 대기
        return self.name