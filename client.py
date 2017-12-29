from socket import *
import threading

s= socket(AF_INET,SOCK_STREAM)

host=''
port=5000
s.connect((host, port))
print("Client Ready")

def goto(linenum):
    global line
    line = linenum

class Client_recieve(threading.Thread):
    def run(self):
        while True:
            data = s.recv(1024)
            print(data.decode())
            if not data:
                break




class Client_send(threading.Thread):
    def run(self):
        while True:
            mess = "Client->"+input()
            s.send(mess.encode())

x=Client_recieve()
y=Client_send()
x.start()
y.start()

