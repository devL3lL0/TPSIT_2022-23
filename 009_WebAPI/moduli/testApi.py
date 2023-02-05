import json
from Config import Connection
from Tabels import Tables
from flask import Flask, jsonify

def open():
    open = False
    while open == False:
        open = Connection.open_connection()
    options = open
    return options

def getPercorsi(cursor):
    cursor.execute(f'''SELECT * FROM {Tables.PERCORSI}''')
    result = cursor.fetchall()
    return result

def getPercorso(id, cursor):
    try:
        id_column = 'id'
        cursor.execute(f'''
                            SELECT {Tables.PERCORSI}.Nome,  FROM {Tables.PERCORSI}
                            ''')
        result = cursor.fetchall()
        result = jsonify({"Success": True, "Result": result})
    except:
        result  = jsonify({"Success": False})
    return result


app = Flask(__name__)

@app.route('/api/v1/percorsi')
def percorsi():
    options = open()
    percorsi = getPercorsi(options[1])
    options[0].close()
    return jsonify(percorsi)

@app.route('/api/v1/percorsi/<id>')
def percorso(id):
    options = open()
    namePercorso = getPercorso(id,options[1])
    options[0].close()
    return jsonify(namePercorso)




def main():
    app.run()

if __name__ == '__main__':
    main()