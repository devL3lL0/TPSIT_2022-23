from flask import Flask, request

app = Flask(__name__)

#decorator -> wrapper --> oggetti che includono altri oggetti
@app.route("/somma", methods = ["GET"])
def somma():
    try:
        a = int(request.args.get('txtA'))
        b = int(request.args.get('txtB'))
        c = a+b
        return f"<h1>Faccio la somma di {a} + {b} = {c}</h1>"
    except:
        return "Passare i parametri nell'url"

@app.route("/somma_post", methods = ["GET"])
def somma():
    try:
        a = int(request.form.get('txtA'))
        b = int(request.form.get('txtB'))
        c = a+b
        return f"<h1>Faccio la somma di {a} + {b} = {c}</h1>"
    except:
        return "Passare i parametri nell'url"

@app.route("/", methods = ["GET"])
def homepage():
    page = '''
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <form action = "/somma_post" method = "POST">
                   <label for = "primoNumero">1° Numero: </label>
                   <input type = "text" id = "primoNumero" name = "txtA"></input>
                   <br>
                   <label for = "secondoNumero">2° Numero: </label>
                   <input type = "text" id = "secondoNumero" name = "txtB"></input>
                   <br>
                   <input type="submit" value = "somma"> 
                </form>
            </body>
            </html>
    '''
    return page

if __name__ == "__main__":
    app.run()

