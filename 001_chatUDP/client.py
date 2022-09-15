from socket import AF_INET, SOCK_DGRAM, socket
import os
import csv

PORT = 5000

def get_ip_locale():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_loc = s.getsockname()[0]
    print("ip locale server: ", ip_loc)
    s.close()
    return ip_loc


def set_ip_broadcast(ip):
    ip = ip.split('.')
    ip_broadcast = ip[0] + '.' + ip[1] + '.' + ip[2] + '.' + '255'
    return ip_broadcast


def mainChatClient():
    running = True
    nome = input("Inserire il nome utente: ")
    ip_loc = get_ip_locale()
    ip_broadcast = set_ip_broadcast(ip_loc)
    with socket(AF_INET, SOCK_DGRAM) as s:
        while running == True:
            mex = input("Inserire il messaggio: ")
            if mex == 'esci' or mex == 'ESCI':
                running = False
            else:
                mex = nome + ',' + mex + ',' + ip_loc + ',' + str(PORT)
                mex = mex.encode()
                s.sendto(mex, (ip_broadcast, PORT))


if __name__ == "__main__":
    path = os.getcwd()
    pathM = path + "\\Chat"
    if os.path.exists(pathM) == False:
        os.chdir(path)
        os.mkdir("Chat")
        os.chdir(pathM)
        os.mkdir("Cronologia")
        cron = pathM + "\\Cronologia\\Cronologia.csv"
        ceck = os.path.isfile(cron)
        pathM = pathM + "\\Cronologia"
        if ceck == False:
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
    else:
        os.chdir(pathM)
    mainChatClient()
