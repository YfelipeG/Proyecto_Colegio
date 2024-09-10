from flask import render_template

from app import app

@app.route("/")
def index():
    return render_template("index.html", titulo="inicio",nombre="Felipe")

@app.route("/hola/<nombre>")
def hola(nombre):
    return render_template("hola.html", Titulo= 'Hola', nombre=nombre)

 