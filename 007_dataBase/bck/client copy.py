from socket import socket, AF_INET, SOCK_STREAM
import time

BUFFER_SIZE = 2048


def main():
    check = False
    running = True
    with socket(AF_INET, SOCK_STREAM) as s:
        s.connect(("127.0.0.1", 8000))
        while check == False or check == 'False':
            data = s.recv(BUFFER_SIZE)
            crd = data.decode('utf8')
            crd = crd.split(';')
            username = input(f'{crd[0]}')
            password = input(f'{crd[1]}')
            s.send((username+','+password).encode('utf8'))
            data = s.recv(BUFFER_SIZE)
            string = data.decode('utf8')
            string = string.split(';')
            check = string[0]
            if string[0] == 'signUp':
                check = False
                answ = input(f'{string[1]}')
                s.send(answ.encode('utf8'))
            else:
                print(string[1])
            time.sleep(1.5)
        while running:
            data = s.recv(BUFFER_SIZE)
            msg = data.decode('utf8')
            answ = input(f"{msg}")
            s.send(answ.encode('utf8'))
            if answ.upper() == 'Y' or answ.upper() == 'YES':
                data = s.recv(BUFFER_SIZE)
                msg = data.decode('utf8')
                msg = msg.split(';')
                if msg[0] == 'search':
                    user = input(f"{msg[1]}")
                    s.send(user.encode('utf8'))
                    data = s.recv(BUFFER_SIZE)
                    user_list = data.decode('utf8')
                    print(user_list)
            time.sleep(1)
        s.close()


if __name__ == '__main__':
    main()