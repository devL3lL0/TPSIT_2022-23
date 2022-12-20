import time
#from AlphaBot import AlphaBot
from AlphaBotDebug import AlphaBotDebug

class lib():
    
    def Robot(robot):
        if robot == 'REALE':
            pass
            #ab = AlphaBot()
        else:
            ab = AlphaBotDebug()
            print("Creata una nuova istanza Alphabot virtuale")
        return ab

    def rec(ab, msg, move):
        if len(move) > 0:
            print("Inizio a muovermi")
            for movement in move:
                print(movement)
                if movement == 'W':
                    ab.forward()
                elif movement == 'D':
                    ab.right()
                elif movement == 'A':
                    ab.left()
                elif movement == 'S':
                    ab.backward()
                elif msg != 'STOP' and msg != 'REC' and msg != 'X':
                    print("Movimento non supportato")
        else:
            print("Registra dei movimenti prima con il comando REC")
        rec = False
        return rec

    def deleteMovement(move):
        move = []
        return move
    
    def showLastMovements(ab, msg, move):
        print('')
        print('Lista movimenti')
        if len(move) > 0:
            for movement in move:
                print(movement)
                if movement == 'W':
                    ab.forward()
                elif movement == 'D':
                    ab.right()
                elif movement == 'A':
                    ab.left()
                elif movement == 'S':
                    ab.backward()
                elif msg != 'STOP' and msg != 'REC' and msg != 'X':
                    print("Movimento non supportato")
        else:
            print('vuota')

    def chekCommand(msg, ab, robot, rec, move, running):
        if rec == True:
            if msg == 'W' or msg ==  'A' or msg == 'S' or msg == 'D':
                print(f"Sto registrando il movimento {msg}")
                move.append(msg)
            else:
                print("Movimento non supportato")
        if msg == 'REC':
            print("Inizio registrazione movimenti")
            rec = True
        if msg == 'STOP':
            if rec != False:
                print("Interruzione registrazione")
                rec = lib.rec(ab, msg, move)
            else:
                print("Attiva prima la registrazione con il comando REC!!")
        if msg == 'W':
            ab.forward()
            time.sleep(3)

        elif msg == 'D':
            ab.right()
            time.sleep(3)

        elif msg == 'A':
            ab.left()
            time.sleep(3)

        elif msg == 'S':
            ab.backward()
            time.sleep(3)
    
        elif msg == 'E':
            print("Uscita dall'ascolto in corso")
            running = False
            move = []
            if robot != 'REALE':
                print("Cancellazione istanza Alphabot virtuale")
            else:
                print("Scollegamento dal robot in corso")
        
        elif msg == 'X':
            if rec == False:
                move = lib.deleteMovement(move)
                print("Movimenti registrati, eliminati con successo")
            else:
                print("Disattiva prima la registrazione con il comando STOP!!") 
        
        elif msg == 'V':
            lib.showLastMovements(ab, msg, move)

        elif msg != 'STOP' and msg != 'REC': 
            print("Comando non supportato")
        
        rec_run_move = [rec, running, move]

        return rec_run_move