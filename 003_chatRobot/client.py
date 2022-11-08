from socket import AF_INET, SOCK_STREAM, socket

def chatClient():
    addres = str(input("Inserire l'ip del robot: "))
    with socket(AF_INET, SOCK_STREAM) as s:
        address = (addres, 3450)
        print(address)
        running = True
        s.connect(address)
        while running == True:
            msg = str(input("Inserire il comando: "))
            msg = msg.upper()
            if msg == 'E':
                running = False
            else:
                s.send(msg.encode('utf8'))


if __name__ == "__main__":
    chatClient()