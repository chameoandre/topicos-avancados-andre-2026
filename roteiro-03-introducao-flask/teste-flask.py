from flask import Flask
app = Flask("Meu sitezinho")

@app.route("/teste")

def teste():
    return "Rota confirmada com sucesso!!"

app.run() 

