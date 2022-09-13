from socket import AF_INET, SOCK_DGRAM, socket 

PORT = 5000

def ip_locale():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_loc = s.getsockname()[0]
    print("ip locale server: ", ip_loc)
    s.close()
    return ip_loc

def mainChatClient():
    running = True
    ip_loc = ip_locale()
    ip_loc = ip_loc.split('.')
    ip_broadcast = ip_loc[0] + '.' + ip_loc[1] + '.' + ip_loc[2] + '.' + '255'
    with socket(AF_INET, SOCK_DGRAM) as s:
        while running == True:
            mex = input("Inserire il messaggio: ")
            if mex == 'esci' or mex == 'ESCI':
                running = False
            else:
                mex = mex.encode()
                s.sendto(mex, (ip_broadcast, PORT))

if __name__ == "__main__":
    mainChatClient()
