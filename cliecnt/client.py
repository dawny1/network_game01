from _thread import *
import socket

    
class socketClient():
    
    HOST = '127.0.0.1'
    PORT = 9999

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        self.x = 0
        self.y = 0
        self.name = ""
        self.arrows =  []
        self.client_run()
        
    def client_run(self):
        #서버로부터 오는 메세지를 대기하는 쓰레드 생성
        start_new_thread(self.recv_data, (self.client_socket,))     
        #클라이언트 무한 대기
        # while True:

    #서버로 부터 메세지를 받는다.    
    def recv_data(self,client_socket):
        while True:
            data = client_socket.recv(1024).decode()
            value = data.split(',')
            print(f"서버메세제:{value},{type(value)}")
            self.x = int(value[0])
            self.y = int(value[1])
            self.name = value[2]

            arrow_len = int(value[3])
            arrows = []

            for i in range(arrow_len):
                x = int(value[i*2+4])
                y = int(value[i*2+5])
                arrows.append([x,y])

            self.arrows = arrows

            # if self.arrow_len == 1:
            #     self.arrow_x1 = int(value[4])
            #     self.arrow_y1 = int(value[5])
            # elif self.arrow_len == 2:
            #     self.arrow_x2 = int(value[6])
            #     self.arrow_y2 = int(value[7])
            #     self.arrow_x3 = -50
            #     self.arrow_y3 = -50
            # elif self.arrow_len == 3:
            #     self.arrow_x3 = int(value[8])
            #     self.arrow_y3 = int(value[9])






            # self.arrow_position_x = []
            # self.arrow_x = int(value[])
            # self.arrow_x = int(value[3])
            # self.arrow_y = int(value[4])


            # is_find = False
            # for user in self.member:
            #     if user.name == self.name:
            #         is_find = True

            # if is_find==False:
            #     user = User(self.screen,0,0,"")
            #     self.member.append(user)
            
            # print(x,type(x))
            
    def send_data(self,rec,name,arrows_position):
        msg = f'{rec.x},{rec.y},{name},{len(arrows_position)}'
        for pos in arrows_position:
            msg += f',{pos[0]},{pos[1]}'
        self.client_socket.send(msg.encode())
        # print(msg)

    
        
