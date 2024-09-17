from flask import jsonify, render_template

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
    try:

        colegio = Colegio.query.get(id)

        if colegio is None:
            return jsonify({"status": "failure", "message": "No existe el colegio"}),404
        
        db.session.delete(colegio)
        db.session.commit()

        return jsonify({"status": 'succes', 'message': 'Colegio eliminado'}),200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}),500