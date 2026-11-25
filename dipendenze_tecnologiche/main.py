from flask import Flask
import random
app = Flask(__name__)



attivita_neve = ['sci', 'snowboard', 'telemark', 'ramponata', 'ciaspolata',]


@app.route("/ciao")
def ciao():
    return "<p>Ciaooo</p>"

@app.route("/ciao/come")
def come():
    return "<p>ciao come stai?</p>"

@app.route("/giorno")
def giorno():
    return "<p>Oggi che giorno è?</p>"

@app.route("/giorno/meteo")
def meteo():

    return "<p>Che tempo fa oggi?</p>"

@app.route("/giorno/meteo/sole")
def sole():

    return "<p>oggi è una giornata assolata☀️</p>"

@app.route("/giorno/meteo/pioggia")
def pioggia():

    return "<p>oggi è una giornata piovosa⛈️</p>"

@app.route("/giorno/meteo/neve")
def neve():

    return "<p>oggi nevica</p>"

@app.route("/giorno/meteo/neve/attività da fare")
def attivita_neve():

    return "<p>è il giorno ideale per fare " + random.choice(attivita_neve) + "</p>"

@app.route("/secret")
def immagini():
    img = random.choice(os.listdir("static/immagini casuali"))   
    return f'<img src="/static/immagini casuali/{img}">'


app.run(debug=True)