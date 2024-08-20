import socket
from _thread import *

class socketServer():
    client_sockets = [] #클라이언트 목록
    HOST = '127.0.0.1'
    PORT = 9999

    def __init__(self):
        print('>> Server Start')
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((self.HOST, self.PORT))
        self.server_socket.listen()
        self.server_run()
        
    #client가 접속되는지 기다리고 쓰레드를 생서한다.
    def server_run(self):
        while True:
            print('>>클라이언트 접속 대기')
            client_socket, addr = self.server_socket.accept()
            self.client_sockets.append(client_socket) #접속된 클라이언트를 리스트에 추가한다.
            print('>> Connected by :', addr[0], ':', addr[1])
            print("연결된 수 : ", len(self.client_sockets))
            
            start_new_thread(self.thread_client, (client_socket, addr)) #클라이언트 쓰레드 생성
                        
    #접속된 client마다 각각 쓰레드가 생성된다.
    def thread_client(self,client_socket, addr):
        
        while True:
            try:
                data = client_socket.recv(1024*10).decode()
                print(f"클라이언트에서 받은 메세지 : {data}")
                msg = f'{data}'
                for client in self.client_sockets:
                    if client_socket != client:#자신을 제외
                        client.send(msg.encode()) #문자를 encode해서 클라이언트에게 보낸다.
            except ConnectionResetError:
                self.client_sockets.remove(client_socket)
                client_socket.close()
                break
                            
server = socketServer()