#APPUNTI DECORATOR PYTHON

def inizio_fine(func):
    def wrapper():
        print('inizio')
        func()
        print('fine')
    return wrapper

@inizio_fine
def ciao():
    print("ciao")
#ciao = inizio_fine(ciao)
@inizio_fine
def hello():
    print("hello")
#hello = inizio_fine(hello)


if __name__ == "__main__":
    ciao()
    hello()