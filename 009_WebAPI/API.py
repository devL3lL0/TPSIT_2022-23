
import json
import sqlite3
from flask import Flask, jsonify, request


# Funzione che restituisce la lista dei percorsi:
def get_percorsi(cursor):
    cursor.execute('''SELECT id, nome FROM PERCORSO''')
    percorsi = cursor.fetchall()
    return [{"id": percorso[0], "nome": percorso[1]} for percorso in percorsi]


# Funzione che restituisce i dettagli di un percorso:
def get_percorso(id, cursor):
    cursor.execute('''SELECT id, nome FROM PERCORSO WHERE id = ?''', (id,))
    percorso = cursor.fetchone()
    mossa = cursor.execute('''SELECT posizione, codMovimento, tempo, nome FROM Mossa, Movimento WHERE codPercorso = ? AND codMovimento = Movimento.id ORDER BY posizione''', (id,))
    mossa = cursor.fetchall()
    print(mossa)
    mosse = [{"id": m[1], "nome": m[3], "tempo": m[2], "posizione": m[0]} for m in mossa]
    return {"id": percorso[0], "nome": percorso[1], "mossa": mosse}


app = Flask(__name__)
# Restituisce il JSON con tutti i percorsi
@app.route("/api/v1/percorsi", methods = ['GET'])
def listaPercorsi(): 
    try:
        # Mi connetto a SQL 
        with sqlite3.connect('./Alphabot.db') as conn:
            cursor = conn.cursor()
            # Eseguo query
            percorsi = get_percorsi(cursor)
            temp = jsonify({"success": True, "result": percorsi})
            # Chiudo connessione a SQL
            return temp
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

@app.route("/api/v1/percorsi", methods = ['POST'])
def creaPercorso():
    try:
        dati = request.get_json()
        #qui metti la query
    except Exception as e:
        return jsonify({"success": False, "error": str(e)})

# Restituisce il JSON con i dettagli del percorso indicato nell'URL
@app.route("/api/v1/percorsi/<id>")
def dettagliPercorso(id):
    conn = sqlite3.connect('./Alphabot.db')
    cursor = conn.cursor()
    percorso = get_percorso(id, cursor) 
    temp= jsonify(percorso) 
    conn.close()
    return temp


def main():
    app.run()

if __name__ == "__main__":
    main()










