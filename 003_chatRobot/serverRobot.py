from socket import AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, socket
import time
#from AlphaBot import AlphaBot
from AlphaBotDebug import AlphaBotDebug


def chatServer():
    quest = input("Robot Virtuale o Reale?: ")
    if quest.upper() == 'REALE':
        #ab = AlphaBot()
        pass
    else:
        ab = AlphaBotDebug()
        print("Creata istanza virtuale")

    ab = AlphaBotDebug()
    ab.stop()
    with socket(AF_INET, SOCK_STREAM) as s:
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", 3450))

        running = True

        s.listen()

        print("In Ascolto")

        client, clientAddress = s.accept()

        move = []
        rec = False
        ab.stop()
        while ab and running == True:
            msg = client.recv(1024).decode('utf8')
            msg = msg.upper()
            while rec == True:
                if rec == True:
                    if msg == 'W' or msg == 'B' or msg == 'L' or msg == 'S':
                        print(f"Sto registrando il movimento {msg}")
                        move.append(msg)
                    elif msg == 'STOP':
                        rec = False
                    else:
                        print("Movimento non supportato")
            if msg == 'REC':
                print("In")
                rec = True
            if msg == 'STOP':
                print("Inizio a muovermi")
                for movement in move:
                    print(movement)
                    if movement == 'W':
                        ab.forward()
                    elif movement == 'R':
                        ab.right()
                    elif movement == 'L':
                        ab.left()
                    elif movement == 'B':
                        ab.backward()
                    else:
                        print("Movimento non supportato")
            if msg == 'W':
                print('sto andando avanti')
                ab.forward()
                time.sleep(3)

            elif msg == 'R':
                ab.stop()
                ab.right()
                time.sleep(3)

            elif msg == 'L':
                ab.stop()
                ab.left()
                time.sleep(3)

            elif msg == 'B':
                ab.stop()
                ab.backward()
                time.sleep(3)

            elif msg == 'E':
                print("Uscita dall'ascolto in corso")
                running = False

            else:
                print("Comando non supportato")
            ab.stop()

        s.close()
    print("Chiusura server effettuata")


if __name__ == "__main__":
    chatServer()
