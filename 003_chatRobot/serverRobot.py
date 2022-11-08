from socket import AF_INET, SOCK_STREAM, socket
import time
from AlphaBot import AlphaBot

def chatServer():
    ab = AlphaBot()
    ab.stop()
    with socket(AF_INET, SOCK_STREAM) as s:
    
        s.bind(("0.0.0.0", 3450))
        
        

        s.listen()
        print("In Ascolto")
        
        client, clientAddress = s.accept()
        
        ab.stop()
        while ab:
            ab.stop()
            
            msg = client.recv(1024).decode('utf8')
            msg = msg.upper()
                
            if msg == 'W':
                print('sto andando avanti')
                ab.forward()
                time.sleep(3)
            elif msg == 'D':
                ab.stop()
                ab.right()
                time.sleep(3)
            ab.stop()


if __name__ == "__main__":
    chatServer()
