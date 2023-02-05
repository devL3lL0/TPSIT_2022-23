import sqlite3 as sq

class LogIn():

    CREDENTIALS = "Type your username: ;Type your password: "
    CONFIRM_SIGNUP = 'False;Singup successfully, please login again...'
    SIGNUP = "signUp;Do you want to signup? [Y/N]: "
    SEARCH = 'search;Type the username to search for: '
    SHOW_USER = 'Would you show all username? [Y/N]: '
    EXIT = 'exit;Do you want to exit? [Y/N]: '
    CONFIRM_SEARCH = "Would you like to search a username? [Y/N]: "
    EXIT = "Do you want to exit? [Y/N]: "
    OPTIONS = 'What do you want to do? [Login/Signup]: '

    def open_connection():
        try:
            conn = sq.connect("./006_dataBase/db/LogIn.db")  # Mi connetto con il db
            print("Connessione al db avvenuta con successo...")
            curs = conn.cursor()
            return (conn, curs)
        except:
            print("Connessione non avvenuta")
            return False

    def close_connection(connection):
        try:
            connection.close()
        except:
            print('Errore nella connessione del db')

    def check_logIn(username, password, cursor):
        try:
            cursor.execute("SELECT username, password FROM UTENTI WHERE username = ? AND password = ?",(username, password))
            result = cursor.fetchall()
            if result == []:
                result = "Username or password are incorrect... try again"
            elif len(result) > 1:
                result = "There is an error with the credentials"
            else:
                result = f"LogIn succesfully, Welcome {result[0][0]}!"
                return (True, result)
            return (False, result)
        except:
            return (False, 'ERROR CONNECTION DATABASE')


    def do_signUp(username, password, connection, cursor):
        try:
            cursor.execute("INSERT INTO UTENTI (username, password) VALUES (?, ?)",(username, password))
            connection.commit()
            return True
        except:
            return False

    def search_username(username, string, cursor):
        try:
            user = '%' + string + '%'
            cursor.execute(  '''SELECT username 
                                FROM UTENTI WHERE (%s) 
                                LIKE ? '''%username,(user,))
            result = cursor.fetchall()
            if result == []:
                result = False
        except:
            result = 'Error'
        return result
    
    def show_username(cursor):
        try:
            cursor.execute(''' SELECT username FROM UTENTI ''')
            result = cursor.fetchall()
            if result == []:
                    result = False
        except:
            result = 'Error'
        return result

    