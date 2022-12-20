import socket
import threading
import time
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("127.0.0.1",8000))
while True:
    msg=s.recv(4096).decode()
    print(msg)
    oper=input("")

    s.sendall((oper).encode())
    if oper=="EXIT":
        s.close()
        break
    msg=s.recv(4096).decode()
    print(msg)




