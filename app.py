from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compras')
def compras():
    return render_template('compras.html',item1='farinha',item2='batata')

@app.route('/mercados')
def mercados():
    return render_template('mercados.html')

@app.route('/gastos', defaults={'mes':'janeiro','valor':'0'})
@app.route('/gastos/<mes>/<valor>')
def gastos(mes, valor):
    return render_template('gastos.html', mes = mes, valor = valor)

@app.route('/dobro/<float:n>')
@app.route('/dobro/<int:n>')
def dobro(n):
    resultado=2*n
    return render_template("dobro.html",n=n,resultado=resultado)