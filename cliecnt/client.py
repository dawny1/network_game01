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
            # print(f"서버메세제:{value},{type(value)}")
            self.x = int(value[0])
            self.y = int(value[1])
            self.name = value[2]

            
            self.player_dir = int(value[3])
            print(arrows)

            arrow_len = int(value[4])
            arrows = []

            for i in range(arrow_len):
                x = int(value[i*3+5])
                y = int(value[i*3+6])
                arrow_dir = int(value[i*3+7])
                arrows.append([x,y,arrow_dir])

            self.arrows = arrows

    def send_data(self,rec,name,player_dir,arrow_dir,arrows_position):
        msg = f'{rec.x},{rec.y},{name},{player_dir},{len(arrows_position)}'
        for pos in arrows_position:
            msg += f',{pos[0]},{pos[1]},{arrow_dir}'
        # msg +=  ",\n"
        self.client_socket.send(msg.encode())

        # print(msg)
    
        
