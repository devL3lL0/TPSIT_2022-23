
import requests
HOST = "http://127.0.0.1:5000"

def getPercorsi():
    percorsi = requests.get(HOST+ "/api/v1/percorsi")
    print(percorsi.content)

def creaPercorso():
    richiesta = {"nome":"quadrato"}
    requests.post(HOST+ "/api/v1/percorsi", json=richiesta)

def main(): 
    #getPercorsi()
    creaPercorso()

if __name__ == "__main__":
    main()