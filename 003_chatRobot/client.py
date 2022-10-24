from socket import AF_INET, SOCK_STREAM, socket

def chatClient():
    with socket(AF_INET, SOCK_STREAM) as s:
        address = ("127.0.0.1", 3450)
        print(address)
        # connetto il client al server
        # come indirizzo utilizzo il localhost
        s.connect(address)
        while True:
        # invio dei dati e codico in utf-8
            s.send("avanti".encode())

        # chiudo la connessione
        s.close()  


if __name__ == "__main__":
    chatClient()