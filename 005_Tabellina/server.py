from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR


class Server(Thread):
    def __init__(self, address):
        self.running = True
        self.client = ""
        self.clientAddress = ""
        self.running = True
        self.address = address

    def run(self):
        with socket(AF_INET, SOCK_STREAM) as s:
            s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            s.bind(self.address)
            print("In Ascolto")
            s.listen()
            self.client, self.clientAddress = s.accept()
            self.listen(self.client)

    def listen(self, s):
        while self.running:
            check = 0
            connection = True
            data = s.recv(4096)
            mex = data.decode('utf8')
            mex = mex.upper()
            if mex == 'CONNESSO':
                while connection:
                    s.send("Inserire il numero per la tabellina: ".encode('utf8'))
                    data = s.recv(4096)
                    n = data.decode()
                    if type(check) == type(n):
                        tab = tabellina(n)
                        s.send(tab.encode('utf8'))
                    else:
                        print("Uscita in corso...")
                        connection = False
            else:
                print("Client non connesso!")
                self.running = False

def tabellina(op):
    i = 1
    res = ""
    while i <= 10:
        ris = op * i
        if i ==1:
            res = str(ris)
        else:
            res = res + ',' + str(ris)
        i += 1
    return res


def main():
    address = ("127.0.0.1", 8000)
    server = Server(address)
    server.run()


if __name__ == '__main__':
    main()
