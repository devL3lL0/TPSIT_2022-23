from socket import AF_INET, SOCK_STREAM, socket

def chatServer():
    with socket(AF_INET, SOCK_STREAM) as s:
        
        #non utilizzo il local host perchè devo connetteremi in tcp
        s.bind(("0.0.0.0", 3450))
        

        #configurano l'host per farlo ascoltare
        s.listen()
        print("In Ascolto")
        #il server si blocca fino a quando il client prova a collegarsi
        #quando prova a collegarsi, restituisce un rif al socket del client
        client, clientAddress = s.accept()
        
        while True:
            #indico i byte che voglio passare e decodifico i bytes
            # il recv puo' restituire -> null oppure dei bytes
            msg = client.recv(1024).decode('utf8')
            print(msg)



# eseguito solo da terminale
if __name__ == "__main__":
    chatServer()