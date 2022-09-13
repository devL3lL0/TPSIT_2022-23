from socket import AF_INET, SOCK_DGRAM, socket 

IP = "192.168.95.255"
PORT = 5000

def mainChatClient():
    running = True
    with socket(AF_INET, SOCK_DGRAM) as s:
        while running == True:
            mex = input("Inserire il messaggio: ")
            if mex == 'esci' or mex == 'ESCI':
                running = False
            else:
                mex = mex.encode()
                s.sendto(mex, (IP, PORT))

if __name__ == "__main__":
    mainChatClient()