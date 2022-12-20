from socket import AF_INET, SOCK_STREAM, socket

def chatClient():
    address = str(input("Inserire l'ip del robot: "))
    with socket(AF_INET, SOCK_STREAM) as s:
        address = (address, 3450)
        running = True
        s.connect(address)
        robot = input("Robot reale o virtuale?: ")
        s.send(robot.upper().encode('utf8'))
        while running == True:
            msg = str(input("Inserire il comando: "))
            msg = msg.upper()
            if msg == 'E':
                running = False
            s.send(msg.encode('utf8'))
        s.close()
    print("Chiusura client effettuata")
if __name__ == "__main__":
    chatClient()