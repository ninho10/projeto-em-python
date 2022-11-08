from flask import Flask

app = Flask(__name__)

# criar a primeira
@app.route("/")
def homepage():
    return "Esse e meu primeiro site em Python"

@app.route("/contatos")
def contatos():
    return "<p>Nossos Contatos </p> <p> celular: (21) 7657876567</p>   <p> Email lxm@cnc.com </p>"


# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)
