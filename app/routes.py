from flask import render_template

from app import app

from app.models import Colegio

@app.route("/")
def index():
    return render_template("index.html", titulo="inicio",nombre="Felipe")


@app.route("/colegio", methods=["GET"])
def tipos_colegio():
    tipos_colegio = Colegio.query.all()
    print(tipos_colegio)
    print(len(tipos_colegio))
    return render_template("colegio.html", titulo="Colegios", tipos_colegio=tipos_colegio)