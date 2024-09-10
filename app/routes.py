from flask import render_template

from app import app

@app.route("/")
def index():
    return render_template("index.html", titulo="inicio",nombre="Felipe")

@app.route("/hola/<nombre>")
def hola(nombre):
    return render_template("hola.html", Titulo= 'Hola', nombre=nombre)

@app.route("/lenguajes-programacion")
def lenguajes():
    lenguajes = ['Python', 'Java', 'JavaScript', 'C#', 'PHP']
    return render_template("lenguajes.html", titulo="Lenguajes de programación", lenguajes=lenguajes)

 