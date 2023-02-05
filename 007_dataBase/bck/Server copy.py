from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
from threading import Thread
from LogIn import LogIn
import time

BUFFER_SIZE = 2048

class Server(Thread):

    def __init__(self, exit, count, check):
        self.esci = exit
        self.count = count
        self.check = check
        self.running = True

    def stop(self):
        self.running = False

    def terminate(self, option):
        self.exit = True
        LogIn.close_connection(option)

    def exit(self, client, option):
        send_credentials(client, LogIn.EXIT)
        data = client.recv(BUFFER_SIZE)
        confirm = data.decode('utf8')
        if confirm.upper() == 'Y' or confirm.upper() == 'YES':
            self.stop()
        time.sleep(1)

    def run(self):
        #VARIABILI DI CONTROLLO CICLI
        check = False
        
        #APERTURA SOCKET TCP
        with socket(AF_INET, SOCK_STREAM) as s:
            s.bind(("0.0.0.0", 8000))
            s.listen()
            print('Server in Ascolto...')

            #CICLO DI VITA
            while self.esci == False:
                client, clientAddress = s.accept()
                options = LogIn.open_connection()
                #options = config()
                print(f"Client {clientAddress[0]} connesso alla porta {clientAddress[1]}")
                while self.count <= 4 and check == False:
                    send_credentials(client, LogIn.CREDENTIALS)
                    crd = receive_credentials_client(client)
                    self.check = LogIn.check_logIn(crd[0], crd[1], options[1])
                    check = self.check[0]
                    if self.check[0] == False:
                        if self.count > 3:
                            try:
                                send_credentials(client, LogIn.SIGNUP)
                                data_Signup = client.recv(BUFFER_SIZE)
                                signup = data_Signup.decode('utf8')
                                if signup.upper() == 'Y' or signup.upper() == 'YES':
                                    send_credentials(client, LogIn.CREDENTIALS)
                                    crd_s = receive_credentials_client(client)
                                    if LogIn.do_signUp(crd_s[0], crd_s[1], options[0], options[1]):
                                        self.count = 0
                                        send_credentials(client, LogIn.CONFIRM_SIGNUP)
                            except:
                                check = True
                        else:
                            send_credentials(client, 'False'+';'+self.check[1])
                            self.count += 1
                    else:
                        send_credentials(client, 'True'+';'+self.check[1])
                    time.sleep(1)
                time.sleep(1)

                while self.running == True:
                    search_user(client, options[1])
                    show_user(client, options[1])
                    self.exit(client, options[0])
                self.terminate(options[0])
        s.close()

def config():
    conn_db = False
    #ITERO FINCHÈ NON STABILISCE LA CONNESSIONE CON IL DB
    while conn_db == False:
        options = LogIn.open_connection()
    return options

#INTERAZIONE CON IL CLIENT
def send_credentials(client, mode):
    client.send(mode.encode('utf8'))
    #mode INTENDE L'AZIONE DA COMUNICARE AL CLIENT

#RICEZIONE DEGLI INPUT DEL CLIENT
def receive_credentials_client(client):
    data = client.recv(BUFFER_SIZE)
    data = data.decode('utf8')
    crd = data.split(',')
    return crd

def show_all_user(option, client):
    username_list = ''
    result = LogIn.show_username(option)
    if result == False:
        username_list = f"No username in db"
    elif result == 'Error server':
        result = 'Error in db'
    else:
        username_list = join_user(username_list, result)
    send_credentials(client, username_list)

def join_user(list, result):
        try:
            for element in result:
                for user in element:
                    list = list + user + ','
        except:
            list = 'Error server'
        return list

def show_search_user(data, client, options):
    username_list = ''
    us_search = data.decode('utf8')
    result = LogIn.search_username('username', us_search, options)
    if result == False:
        username_list = f"No username with {us_search}"
    else:
        username_list = join_user(username_list, result)
    send_credentials(client, username_list)

def show_user(client, option):
    send_credentials(client, LogIn.SHOW_USER)
    data = client.recv(BUFFER_SIZE)
    confirm = data.decode('utf8')
    print(confirm)
    if confirm.upper() == 'Y' or confirm.upper() == 'YES':
        show_all_user(option, client)
        print("Error Server")
    time.sleep(1)

def search_user(client, option):
    confirm = ''
    send_credentials(client, LogIn.CONFIRM_SEARCH)
    data = client.recv(BUFFER_SIZE)
    confirm = data.decode('utf8')
    if confirm.upper() == 'Y' or confirm.upper() == 'YES':
        time.sleep(1)
        send_credentials(client, LogIn.SEARCH)
        data = client.recv(BUFFER_SIZE)
        show_search_user(data, client, option)  
    time.sleep(1)

