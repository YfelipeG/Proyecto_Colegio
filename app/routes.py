from flask import jsonify, render_template, request

from app import app, db

from app.models import Colegio, Grado, Materia

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
            return jsonify({"status": "failure", "message": "Colegio no encontrado "}),404
        
        db.session.delete(colegio)
        db.session.commit()

        return jsonify({"status": 'success', 'message': 'Colegio eliminado'}),200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}),500
    


@app.route("/colegio", methods=["POST"])
def colegio_create():
    try:
        data = request.get_json()
        colegio = Colegio(    
        nit = data.get("nit"),
        nombre = data.get("nombre"),
        direccion = data.get("direccion"),
        telefono = data.get("telefono"),
        correo = data.get("correo"),
        )
        db.session.add(colegio)
        db.session.commit()

        return jsonify({"status": "success", "message": "Colegio creado", 'data':{
            'id': colegio.id,
            'nit': colegio.nit,
            'nombre': colegio.nombre,
            'direccion': colegio.direccion,
            'telefono': colegio.telefono,
            'correo': colegio.correo,
        } }),201

    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}),500
    

@app.route("/colegio/<int:id>", methods=['PUT'])
def colegio_update(id):
    try:
        data = request.get_json()
        colegio = Colegio.query.get(id)

        if colegio is None:
            return jsonify({"status": "failure", "message": "Colegio no encontrado "}),404

        colegio.nit = data.get("nit")
        colegio.nombre = data.get("nombre")
        colegio.direccion = data.get("direccion")
        colegio.telefono = data.get("telefono")
        colegio.correo = data.get("correo")
        colegio.updated_at = db.func.current_timestamp()

        db.session.commit()

        return jsonify({"status": "success", "message": "Colegio actualizado", 'data':{
            'id': colegio.id,
            'nit': colegio.nit,
            'nombre': colegio.nombre,
            'direccion': colegio.direccion,
            'telefono': colegio.telefono,
            'correo': colegio.correo,
        } }),200

    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}),500
    
@app.route("/materia", methods=["GET"])
def materia():
    """
    Muestra la lista de materias.
    """

    entidades = Materia.query.all()
    return render_template("materia.html", titulo="Materias", entidades=entidades)  

@app.route("/materia", methods=["POST"])
def materia_create():
    try:
        data = request.get_json()
        entidad = Materia(nombre = data.get("nombre"))

        db.session.add(entidad)
        db.session.commit()

        return jsonify({"status": "success", "message": "Materia creada", 'data':{
            'id': entidad.id,
            'nombre': entidad.nombre,
        } }),201

    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}),500
    
@app.route("/materia/<int:id>", methods=['PUT'])  
def materia_update(id):
    try:
        data = request.get_json()
        entidad = Materia.query.get(id)

        if entidad is None:
            return jsonify({"status": "failure", "message": "Materia no encontrada "}),404

        entidad.nombre = data.get("nombre")
        entidad.updated_at = db.func.current_timestamp()

        db.session.commit()

        return jsonify({"status": "success", "message": "Materia actualizada", 'data':{
            'id': entidad.id,
            'nombre': entidad.nombre,
        } }),200

    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}),500
    

@app.route("/materia/<int:id>", methods=["DELETE"])
def eliminar_materia(id):
    try:

        entidad = Materia.query.get(id)

        if entidad is None:
            return jsonify({"status": "failure", "message": "Materia no encontrada "}),404
        
        db.session.delete(entidad)
        db.session.commit()

        return jsonify({"status": 'success', 'message': 'Materia eliminada'}),200
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}),500


@app.route("/grado", methods=["GET"])
def grado():
    """
    Muestra la lista de materias.
    """

    entidades = Grado.query.all()
    return render_template("grado.html", titulo="Grados", entidades=entidades) 

@app.route("/grado", methods=["POST"])
def grado_create():
    try:
        data = request.get_json()
        entidad = Grado(nombre = data.get("nombre"))

        db.session.add(entidad)
        db.session.commit()

        return jsonify({"status": "success", "message": "Grado creado", 'data':{
            'id': entidad.id,
            'nombre': entidad.grado,
            'descripcion': entidad.descripcion,
        } }),201

    except Exception as e:
        db.session.rollback()
        return jsonify({"status": "error", "message": str(e)}),500