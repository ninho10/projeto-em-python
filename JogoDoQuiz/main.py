from flask import Flask, render_template, redirect, request


app = Flask(__name__)
app.config['SECRET_KEY'] = 'NINHO'


@app.route('/login2')
def home():

    return render_template('login2.html')


@app.route('/login2', methods=['POST'])
def login2():

    nome = request.form.get('nome')
    senha = request.form.get('senha')

    if nome == 'ninho' and senha == '123':
        return render_template('quiz.py')
    else:
        return redirect('/login2')


if __name__ in "__main__":
    app.run(debug=True)
