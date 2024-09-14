from app import app, db
import datetime
from sqlalchemy import func


class Estudiante(db.Model):
    """
    Representa un estudiante.
    """

    __tablename__ = 'estudiante'
    documento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellidos = db.Column(db.String(45), nullable=False)
    telefono = db.Column(db.String(45))
    email = db.Column(db.String(45), unique=True)
    direccion = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    colegio_id = db.Column(db.Integer, db.ForeignKey('colegio.id'))
    grado_id = db.Column(db.Integer, db.ForeignKey('grado.id'))

    def __repr__(self):
        return f'<Estudiante {self.nombre} {self.apellidos}>'
    


class Colegio(db.Model):
    __tablename__ = 'colegio'
    id = db.Column(db.Integer, primary_key=True)
    nit = db.Column(db.String(32), unique=True, nullable=False)
    nombre = db.Column(db.String(45), nullable=False)
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.String(16))
    correo = db.Column(db.String(64), unique=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f'<Colegio {self.nombre}>'



class Materia(db.Model):
    __tablename__ = 'materia'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    estudiante_documento = db.Column(db.Integer, db.ForeignKey('estudiante.documento'))

    def __repr__(self):
        return f'<Materia {self.nombre}>'
    



class Grado(db.Model):
    __tablename__ = 'grado'
    id = db.Column(db.Integer, primary_key=True)
    grado = db.Column(db.String(45), nullable=False)
    descripcion = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    colegio_id = db.Column(db.Integer, db.ForeignKey('colegio.id'))
    materia_id = db.Column(db.Integer, db.ForeignKey('materia.id'))

    def __repr__(self):
        return f'<Grado {self.grado}>'
    



class Usuario(db.Model):
    __tablename__ = 'usuario'
    id = db.Column(db.Integer, primary_key=True)
    documento = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)
    nombre = db.Column(db.String(45), nullable=False)
    apellidos = db.Column(db.String(45), nullable=False)
    email = db.Column(db.String(64), unique=True, nullable=False)
    direccion = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'))

    def __repr__(self):
        return f'<Usuario {self.nombre} {self.apellidos}>'
    


class Rol(db.Model):
    __tablename__ = 'rol'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    descripcion = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __repr__(self):
        return f'<Rol {self.nombre}>'
    
with app.app_context():

    db.create_all()