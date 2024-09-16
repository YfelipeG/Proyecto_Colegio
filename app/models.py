from datetime import datetime
from sqlalchemy import event

from app import app, db
from sqlalchemy import func
  

class Colegio(db.Model):
    __tablename__ = 'colegio'

    id = db.Column(db.Integer, primary_key=True)
    nit = db.Column(db.String(32), unique=True, nullable=False)
    nombre = db.Column(db.String(64), nullable=False)
    direccion = db.Column(db.String(255))
    telefono = db.Column(db.String(16))
    correo = db.Column(db.String(64), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # Relaciones
    estudiantes = db.relationship('Estudiante', back_populates='colegio')
    grados = db.relationship('Grado', back_populates='colegio')
    usuarios = db.relationship('Usuario', back_populates='colegio')

    def __repr__(self):
        return f'<Colegio {self.nombre}>'


class Estudiante(db.Model):
    __tablename__ = 'estudiante'

    documento = db.Column(db.Integer, primary_key=True)
    nombres = db.Column(db.String(45), nullable=False)
    apellidos = db.Column(db.String(45), nullable=False)
    telefono = db.Column(db.String(45))
    email = db.Column(db.String(45), unique=True)
    direccion = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    colegio_id = db.Column(db.Integer, db.ForeignKey('colegio.id'))
    grado_id = db.Column(db.Integer, db.ForeignKey('grado.id'))

    # Relaciones
    colegio = db.relationship('Colegio', back_populates='estudiantes')
    grado = db.relationship('Grado', back_populates='estudiantes')
    usuarios = db.relationship('Usuario', back_populates='estudiante')

    def __repr__(self):
        return f'<Estudiante {self.nombres} {self.apellidos}>'


class Grado(db.Model):
    __tablename__ = 'grado'

    id = db.Column(db.Integer, primary_key=True)
    grado = db.Column(db.String(45), nullable=False)
    descripcion = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    colegio_id = db.Column(db.Integer, db.ForeignKey('colegio.id'))
    materia_id = db.Column(db.Integer, db.ForeignKey('materia.id'))

    # Relaciones
    estudiantes = db.relationship('Estudiante', back_populates='grado')
    colegio = db.relationship('Colegio', back_populates='grados')
    materia = db.relationship('Materia', back_populates='grados')

    def __repr__(self):
        return f'<Grado {self.grado}>'


class Materia(db.Model):
    __tablename__ = 'materia'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # Relaciones
    grados = db.relationship('Grado', back_populates='materia')

    def __repr__(self):
        return f'<Materia {self.nombre}>'


class Rol(db.Model):
    __tablename__ = 'rol'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    descripcion = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # Relaciones
    usuarios = db.relationship('Usuario', back_populates='rol')

    def __repr__(self):
        return f'<Rol {self.nombre}>'


class Usuario(db.Model):
    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True)
    documento = db.Column(db.String(16), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)
    nombre = db.Column(db.String(45), nullable=False)
    apellidos = db.Column(db.String(32), nullable=False)
    telefono = db.Column(db.String(16))
    email = db.Column(db.String(64), unique=True)
    direccion = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)
    rol_id = db.Column(db.Integer, db.ForeignKey('rol.id'))
    colegio_id = db.Column(db.Integer, db.ForeignKey('colegio.id'))
    estudiante_documento = db.Column(db.Integer, db.ForeignKey('estudiante.documento'))

    # Relaciones
    rol = db.relationship('Rol', back_populates='usuarios')
    colegio = db.relationship('Colegio', back_populates='usuarios')
    estudiante = db.relationship('Estudiante', back_populates='usuarios')

    def __repr__(self):
        return f'<Usuario {self.nombre} {self.apellidos}>'





def insert_initial_values():
    if not Colegio.query.first():
        data = [
            Colegio(id= 1, nit='123456789', nombre='Colegio Campestre Aire Libre', direccion='Calle 1 # 2-3', telefono='1234567', correo = 'Aire@gmail.com', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
    ]
        db.session.bulk_save_objects(data)
        db.session.commit()

with app.app_context():
    db.create_all()

    insert_initial_values()