from Packet import Packet
from socket import socket, AF_INET, SOCK_DGRAM
import time

def run_client():
    receiver = ("127.0.0.1", 5000)
    with socket(AF_INET, SOCK_DGRAM) as s:
        with open("Pdf_prova.pdf", "rb") as f:
            s.sendto(Packet(Packet.NEW_FILE, b'').to_bytes(), receiver)
            data = True
            while data:
                data = f.read(4096)
                if data:
                    s.sendto(Packet(Packet.GO_ON, data).to_bytes(), receiver)
                    #time.sleep(0.001)

            s.sendto(Packet(Packet.END_FILE, b'').to_bytes(), receiver)

if __name__ == "__main__":
    run_client()