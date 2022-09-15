from socket import AF_INET, SOCK_DGRAM, socket
import os
import csv

PORT = 5000

# OTTENGO L'IP LOCALE DEL CLIENT
def get_ip_locale():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_loc = s.getsockname()[0]
    print("ip locale server: ", ip_loc)
    s.close()
    return ip_loc

# SETTO L'IP DI BROADCAST
def set_ip_broadcast(ip):
    ip = ip.split('.')# SPLITTO L'IP LOCALE 
    ip_broadcast = ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + '255' # RICOSTRUISCO L'IP METTENDO COME ULTIMO CAPO 255
    return ip_broadcast


def mainChatClient():
    running = True
    nome = input("Inserire il nome utente: ")
    ip_loc = get_ip_locale()
    ip_broadcast = set_ip_broadcast(ip_loc)
    with socket(AF_INET, SOCK_DGRAM) as s: # APRO IL SOCKET
        while running == True:
            mex = input("Inserire il messaggio: ")
            if mex == 'esci' or mex == 'ESCI': # SE IL MESSAGGIO IN INPUT è UGUALE A ESCI o esci CHIUDO IL CLIENT 
                running = False
            else:
                mex = nome + ',' + mex + ',' + ip_loc + ',' + str(PORT) # ALTRIMENTI INVIO IL MESSAGGIO CONCATENANDO ANCHE IP, PORTA, NOME UTENTE
                mex = mex.encode() # CODIFICO 
                s.sendto(mex, (ip_broadcast, PORT)) # INVIO


if __name__ == "__main__":
    path = os.getcwd() # OTTENGO IL PERCORSO DI DOVE MI TROVO NELL'ESPLORA RISORSE
    pathM = path + "\\Chat" # CONTROLLO SE LA CARTELLA "Chat" ESISTE
    if os.path.exists(pathM) == False: 
        os.chdir(path)
        os.mkdir("Chat") # LA CREO
        os.chdir(pathM)
        os.mkdir("Cronologia") # CREO LA CARTELLA "Cronologia"
        cron = pathM + "\\Cronologia\\Cronologia.csv" # CREO IL FILE DELLA CRONOLOGIA
        ceck = os.path.isfile(cron) # CONTROLLO SE ESISTE
        pathM = pathM + "\\Cronologia"
        if ceck == False: # LO CREO
            os.chdir(pathM)
            with open("Cronologia.csv", "w", newline="")as file:
                writer = csv.writer(file, delimiter=",")
                header = (["NOME", "INDIRIZZO_IP", "MESSAGGIO", "DATA", "ORA"])
                writer.writerow(header)
                file.close()
        else:
            cron = pathM + "\\Cronologia\\Cronologia.csv"
            ceck = os.path.isfile(cron)
            if ceck == False:
                os.chdir(pathM)
                with open("Cronologia.csv", "w", newline="")as file:
                    writer = csv.writer(file, delimiter=",")
                    header = (["NOME", "INDIRIZZO_IP",
                              "MESSAGGIO", "DATA", "ORA"])
                    writer.writerow(header)
                    file.close()
    else: # MI POSIZIONO NELLA CARTELLA "Chat"
        os.chdir(pathM)
    mainChatClient()
