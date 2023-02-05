import threading
import time

X = 0

def funzione_num(num):
    global X
    print(f"Partenza del thread {num}")
    print(f"Elaboro...thread {num}")
    time.sleep(0.1)
    for _ in range(10000):
        X = X + 1
    print(f"Finito lavoro del thread {num} con X = {X}")

#il main di default è già un thread "MainThread"  
def main():
    lista_threads = []
    
    for i in range(1000):
        lista_threads.append(threading.Thread(target=funzione_num, args=(i,)))
    
    for k in range(len(lista_threads)):
        lista_threads[k].start()
        
    for j in range(len(lista_threads)):
        lista_threads[j].join()
        
    print("Fine chiamata main.")
    print(f"VALORE FINALE VARIABILE -> {X}")
    if X != (1000*10000): #il risultato dovrebbe essere (1000*10000)
        print("Si è verificato un fenomeno di Race Condition")
    
if __name__ == "__main__":
    main()