import sqlite3 as sq
from Tabels import Tables

class Connection():
    def open_connection():
        try:
            # Provo a connettermi con il db tramite i percorsi 
            try:
                conn = sq.connect(f"./{Tables.PATH1}")
            except:
                try:
                    conn = sq.connect(f"./{Tables.PATH2}")
                except:
                    conn = sq.connect(f"./{Tables.PATH3}")
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