import socket
from _thread import *
import time
class socketServer():
    client_sockets = {}#[] #클라이언트 목록
    HOST = '127.0.0.1'
    PORT = 9999
    player = []

    player_pos = [[100,200],[600,200]]
    player_info = {}
    once = 0
    blocks = '18,150,950,200,900,250,900,300,900,350,900,400,900,450,900,500,900,550,900,600,900,650,900,700,900,750,900,800,950,100,800,850,800,50,750,900,750,'#블럭
    start_pos=[0,950]
    def __init__(self):
        print('>> Server Start')
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen()
        self.server_run()
        self.msg = ""
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

            #self.client_sockets.append(client_socket) #접속된 클라이언트를 리스트에 추가한다.
            # print(self.client_sockets)
            if len(self.client_sockets) == 0:                
                self.client_sockets[addr[1]] = [self.start_pos[0],client_socket,""]
            else:
                pos_find = -1
                for clinet in self.client_sockets:
                    # print(self.client_sockets[clinet])
                    for pos in self.start_pos:
                        if pos != self.client_sockets[clinet][0]: 
                            pos_find = pos
                            break
                    if pos_find != -1:
                        break

                self.client_sockets[addr[1]] = [pos_find,client_socket,""]

            # print(self.client_sockets)
            # self.player.append(addr[1])
            print('>> Connected by :', addr[0], ':', addr[1])
            print("연결된 수 : ", len(self.client_sockets))



            start_new_thread(self.thread_client, (self.client_sockets[addr[1]], addr)) #클라이언트 쓰레드 생성   
            # print(self.client_sockets)
            # print(self.player_info)

            # 처음 = 0
            #두번째 = 1
            #첫번째가 나가면 = 


            # if len(self.client_sockets) <= 1:
            #     print("aaaaa")
            #     msg = f'{self.blocks}{self.start_pos_1}'
            #     client_socket.send(msg.encode())
                
            # else:#두번째 이후 전부
            #     print("bbbbb")
            #     msg = f'{self.blocks}{self.start_pos_2}'
            #     client_socket.send(msg.encode())
            #     # print("1 = ",self.client_sockets[1])


            # if client_socket != client_socket:
            # print(self.msg,"aa",self.player)



    #접속된 client마다 각각 쓰레드가 생성된다.
    def thread_client(self,client_socket,addr):
        msg_src = f'{self.blocks}{client_socket[0]},200,'
        print("a",addr[1],msg_src)
        client_socket[1].send(msg_src.encode())
        time.sleep(2)
        for client in self.client_sockets:
            if client_socket[1] != self.client_sockets[client][1]:#자신을 제외                
                msg = self.client_sockets[client][2]
                print("b",addr[1],msg)
                client_socket[1].send(msg.encode())
                break

        while True:
            try:         
                data = client_socket[1].recv(1024*10).decode()
                # print(data)
                # value = data.split(',')
                # self.player_addr = int(value[2])
                # self.player.append(self.player_addr)
                # print("aaa",self.player)
                # print("aaa",self.player_addr)
                msg = f'{msg_src}'
                msg += f'{data}'
                # print(msg)
                client_socket[2] = msg
                for client in self.client_sockets:
                    if client_socket[1] != self.client_sockets[client][1]:#자신을 제외
                        # print("send",client)
                        self.client_sockets[client][1].send(msg.encode()) #문자를 encode해서 클라이언트에게 보낸다.
            except ConnectionResetError:
                print("aaaaaaaaaa",KeyError)
                # self.client_sockets.remove(client_socket)
                client_socket[1].close()
                del self.client_sockets[addr[1]]

                # del self.player_info[addr[1]]
                # print(self.player_info)
                break
                            
server = socketServer()
