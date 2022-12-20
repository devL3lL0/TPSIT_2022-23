from socket import socket, AF_INET, SOCK_STREAM


def client(address):
    run = True
    with socket(AF_INET, SOCK_STREAM) as s:
        try:
            s.connect(address)
            print("Client connesso!!")
            m = "connesso"
            m = m.upper()
            s.send(m.encode('utf8'))
            while run == True: 
                data = s.recv(4096)
                tab = input(f"{data.decode('utf8')}")
                s.send(tab.encode('utf8'))

                data = s.recv(4096)
                ris = data.decode('utf8')
                
                print("stampo tabellina")
                stampaTabellina(tab, ris)
        except:
            print("Client non connesso!!")

def stampaTabellina(n, ris):
    i = 0
    ris = ris.split(',')
    while i < 10:
        print(f"{n} x {i+1} = {ris[i]}")
        i += 1

def main():
    ip = input("Inserire indirizzo ip server: ")
    port = 8000
    address = (ip, port)
    client(address)

if __name__ == '__main__':
    main()