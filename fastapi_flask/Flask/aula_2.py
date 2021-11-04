from flask import Flask, request


app = Flask(__name__)

@app.route("/") #porta principal
def hello_world():
    return "<p>Hello World!</p>"

@app.route("/novarota") #segunda porta
def novarota():
    return "<h2>Esta é a nova rota</h2>"

@app.route("/outranovarota/<valor>") #inserindo outro valor dentro do endereço
def outranovarota(valor):
    return f"<h2>O valor informado foi {valor}</h2>"

@app.route("/api", methods = ["GET", "POST"]) #mover um json
def api():
    if request.method == "POST":
        return request.get_json()
    else:
        return "Requisição GET"


"""
Para roda api local: 
1 - export FLASK_APP=aula_2.py
2 - flask run
"""