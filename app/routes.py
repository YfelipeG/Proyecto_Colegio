from flask import render_template

from app import app, db

from app.models import Colegio

@app.route("/")
def index():
    return render_template("index.html", titulo="inicio",nombre="Felipe")


@app.route("/colegio", methods=["GET"])
def tipos_colegio():
    tipos_colegio = Colegio.query.all()
    return render_template("colegio.html", titulo="Colegios", tipos_colegio=tipos_colegio)

@app.route("/colegio/<int:id>", methods=["DELETE"])
def eliminar_colegio(id):
    colegio = Colegio.query.get(id)

    if colegio is None:
            return {
        'status': 'failure', 
        'data': None
    }, 204
    
    db.session.delete(colegio)
    db.session.commit()

    return {
        'status': 'success', 
        'data': {
            'id': colegio.id,
        'nombre': colegio.nombre,
        }
    }, 204