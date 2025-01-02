from _thread import *
import socket

class socketClient():
    
    HOST = '127.0.0.1'
    PORT = 9999

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        self.client_run()
        self.x = -100
        self.y = -100
        self.addr = None

        self.game_state = 0
        self.name = ""
        self.hp = 1

        self.arrows =  []

        self.start_x = 0
        self.start_y = 0
        self.player_dir = 0

        self.block_pos = []
        
        
    def client_run(self):
        #서버로부터 오는 메세지를 대기하는 쓰레드 생성
        start_new_thread(self.recv_data, (self.client_socket,))     
        #클라이언트 무한 대기
        # while True:
        
    #서버로 부터 메세지를 받는다.    
    def recv_data(self,client_socket):
        while True:
            try:
                data = client_socket.recv(1024).decode()
                value = data.split(',')
                value = value.copy()
                print(f"서버메세제:{value}")

                cnt = 0
                block_len = int(value[cnt])
                cnt+=1

                block_pos = []
                for i in range(block_len):
                    block_pos.append([int(value[cnt+0]),int(value[cnt+1])])
                    cnt+=2
                self.block_pos = block_pos.copy()

                self.start_x = int(value[cnt])
                cnt+=1
                self.start_y = int(value[cnt])    
                cnt+=1
                if self.game_state == 1:
                    self.x = int(value[cnt])
                    cnt+=1
                    self.y = int(value[cnt])
                    cnt+=1
                    self.name = value[cnt]
                    cnt+=1
                    self.hp = int(value[cnt])
                    cnt+=1

                    self.player_dir = int(value[cnt])
                    cnt+=1

                    arrow_len = int(value[cnt])
                    cnt+=1

                    arrows = []
                    for i in range(arrow_len):
                        x = int(value[cnt])
                        cnt+=1
                        y = int(value[cnt])
                        cnt+=1
                        arrow_dir = int(value[cnt])
                        cnt+= 1
                        arrows.append([x,y,arrow_dir])
                        

                    self.arrows = arrows
            except Exception as ex:
                print(ex)

    def send_data(self,rec,name,hp,player_dir,arrow_dir,arrows_position):
        msg = f'{rec.x},{rec.y},{name},{hp},{player_dir},{len(arrows_position)}'
        for pos in arrows_position:
            msg += f',{pos[0]},{pos[1]},{arrow_dir}'
        # msg +=  ",\n"
        self.client_socket.send(msg.encode())
        # print(msg)
    
        
