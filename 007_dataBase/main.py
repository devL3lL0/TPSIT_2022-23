from Server import Server

def main():
    count = 0
    check = False
    exit = False
    server = Server(exit, count, check)
    server.run()
    
if __name__ == "__main__":
    main()