from flask import render_template

from app import app

@app.route("/")
def index():
    return render_template("index.html", titulo="inicio",nombre="Felipe")


@app.route("/colegio", methods=["GET"])
def colegio():
    tipos_vehiculo = []
    return render_template("colegio.html", titulo="Colegios", tipos_vehiculos=tipos_vehiculo)