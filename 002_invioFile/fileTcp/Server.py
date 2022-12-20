from Packet import Packet
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import os

MAX_SIZE = 7000

def write_file(buffer):
    with open("result.pdf", "wb") as f:
        f.write(buffer)

def run_server():
    os.getcwd()
    os.chdir('c:\\Users\\L3lL0\\OneDrive\\Documenti\\computer\\scuola\\tpsit\\5Brob\TPSIT_2022-23\\002_invioFile\\fileTcp')
    
    with socket(AF_INET, SOCK_STREAM) as s:
        # SE IL SOCKET RIMANE APERTO LO RIUTILIZZA
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        s.bind(("0.0.0.0", 5000))

        s.listen()
        print("In Ascolto")

        client, clientAddress = s.accept()
        print(f"Si è connesso: {clientAddress[0]} con successo alla porta {clientAddress[1]}")
        running = True
        while running:
            msg = client.recv(MAX_SIZE)
            packet = Packet.from_bytes(msg)
            if packet.status == Packet.NEW_FILE:
                file = []
                print('file creato')

            if packet.data and len(packet.data) > 0:
                file.append(packet.data)
                print("Pacchetto ricevuto")

            if packet.status == Packet.END_FILE:
                print("Ricezione pacchetti eseguita")
                print('inizio scrittura file')
                write_file(b''.join(file))
                print("Scrittura file eseguita")
                running = False

if __name__ == "__main__":
    run_server()