from socket import AF_INET, SOCK_DGRAM, socket

BUFFER_SIZE = 4096

mystr = "ciao" # str
# bytes

# POSSIBILITÀ
# LocalHOST = "127.0.0.1"
# HOST = "192.168.37.1"
HOST = "0.0.0.0"
PORT = 5000

def mainChatServer():
    running = True
    with socket (AF_INET, SOCK_DGRAM) as s:
        s.bind((HOST, PORT))
        print('In ascolto')
        while running == True:
            msg = s.recvfrom(BUFFER_SIZE)
            msg = msg[0].decode()
            print(msg)
    
if __name__ == "__main__":
    mainChatServer()
