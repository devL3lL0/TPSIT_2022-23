import threading
import socket
import time


def server(conn, adress):
    print(f"Connesso con {adress}")
    while True:
        conn.sendall("Inserisci un operazione aritmetica".encode())
        msg = conn.recv(4096).decode()
        print(msg)
        if msg == "EXIT":
            print("CIAO")
            conn.close()
            break

        else:
            try:

                risul = eval(msg)
                # COMMENTARE QUESTA RIGA E DECOMMENTARE LE 2 SOTTO PER UTILIZZARE LA SOL2
                conn.sendall(str(risul).encode())
                #risul2 = f"{msg}={int(risul)}"#SOLUZIONE2
                #conn.sendall(str(risul2).encode())#SOLUZIONE2

            except:
                print("Errore")
                conn.sendall("ERRORE".encode())
                pass


def main():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("127.0.0.1", 8000))
    s.listen()
    while True:
        conn, adress = s.accept()
        t = threading.Thread(target=server, args=(conn, adress,))
        t.start()


if __name__ == "__main__":
    main()
