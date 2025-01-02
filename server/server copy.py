import socket
from _thread import *

class socketServer():
    client_sockets = [] #클라이언트 목록
    HOST = '127.0.0.1'
    PORT = 9999
    player = []

    player_pos = [[100,200],[600,200]]
    player_info = {}
    once = 0

    def __init__(self):
        print('>> Server Start')
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen()
        self.server_run()
        self.start_pos = ""
        self.msg = ""
        self.blocks = ""
        self.block_len = []
        self.player_addr = 0
        # self.player_pos = {
        #     len(self.client_sockets) == 1 : '111'
        # } 

    #client가 접속되는지 기다리고 쓰레드를 생서한다.
    def server_run(self):
        while True:
            print('>>클라이언트 접속 대기')
            client_socket, addr = self.server_socket.accept()
            self.client_sockets.append(client_socket) #접속된 클라이언트를 리스트에 추가한다.
            # self.player.append(addr[1])
            print('>> Connected by :', addr[0], ':', addr[1])
            print("연결된 수 : ", len(self.client_sockets))
            start_new_thread(self.thread_client, (client_socket, addr)) #클라이언트 쓰레드 생성   
            print(client_socket)
            if len(self.player_info)==0:
                self.player_info[addr[1]] = '100,200,'
            else:
                if self.once == 1:
                    if self.start_pos == '100,200,':
                        # print("aa")
                        self.player_info[addr[1]] = '700,200,'  
                    else:
                        # print("bb")
                        self.player_info[addr[1]] = '100,200,'
                else:
                    # print("cc")
                    self.player_info[addr[1]] = '700,200,'  
                    self.once = 1
                if len(self.player_info) == 0:
                    # print("dd")
                    self.once = 0

            # 처음 = 100 
            # 두번째  = 200            
            # 두번째가 나가면 = 200
            # 처음이 나가면 = 100

            # a한테는 100만
            # b한테는 200만

            self.blocks = '7,200,100,150,950,200,900,250,900,250,850,300,850,350,800,'#블럭
            self.start_pos = self.player_info[addr[1]]
            self.msg = f'{self.blocks}{self.start_pos}'
            if client_socket != client_socket:
                client_socket.send(self.msg.encode())
            else:
                pass
            # print(self.msg,"aa",self.player)



    #접속된 client마다 각각 쓰레드가 생성된다.
    def thread_client(self,client_socket,addr):
        
        while True:
            try:         
                data = client_socket.recv(1024*10).decode()
                # print(data)
                # value = data.split(',')
                # self.player_addr = int(value[2])
                # self.player.append(self.player_addr)
                # print("aaa",self.player)
                # print("aaa",self.player_addr)
                msg = f'{self.msg}'
                msg += f'{data}'
                # print(msg)
                
                for client in self.client_sockets:
                    if client_socket != client:#자신을 제외
                        client.send(msg.encode()) #문자를 encode해서 클라이언트에게 보낸다.
            except ConnectionResetError:
                self.client_sockets.remove(client_socket)
                client_socket.close()
                del self.player_info[addr[1]]
                break
                            
server = socketServer()


# <socket.socket fd=376, family=2, type=1, proto=0, laddr=('127.0.0.1', 9999), raddr=('127.0.0.1', 4467)>