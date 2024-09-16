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
    
    if not Materia.query.first():
        data = [
            Materia(id= 1, nombre='Matematicas', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
            Materia(id= 2, nombre='Ciencias Naturales', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
            Materia(id= 3, nombre='Ciencias Sociales', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
            Materia(id= 4, nombre='Lenguaje', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
            Materia(id= 5, nombre='Ingles', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
    ]
        db.session.bulk_save_objects(data)
        db.session.commit()

    if not Rol.query.first():
        
        data = [
            Rol(id= 1, nombre='Administrador', descripcion='Administrador del sistema', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
            Rol(id= 2, nombre='Secretaria', descripcion='Secretaria del colegio', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
            Rol(id= 3, nombre='Coordinador', descripcion='Coordinador del colegio', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
            Rol(id= 4, nomnre='Rector', descripcion='Rector del colegio', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
            Rol(id= 5, nombre='Profesor', descripcion='Profesor de una materia', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
            Rol(id= 6, nombre='Psicoloco', descripcion='Psicologo del colegio', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
            Rol(id= 7, nombre='Estudiante', descripcion='Estudiante del colegio', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
            Rol(id= 8, nombre='Acudiente', descripcion='Acudiente de un estudiante', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15)),
    ]
        db.session.bulk_save_objects(data)
        db.session.commit()

    if not Grado.query.first():
        data = [
            Grado(id= 1, grado='Jardin', descripcion='Jardin de infantes', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15), colegio_id=1, materia_id=1),
            Grado(id= 2, grado='Prejardin', descripcion='Prejardin de infantes', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15), colegio_id=1, materia_id=2),
            Grado(id= 3, grado='Primero', descripcion='Primero de primaria', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15), colegio_id=1, materia_id=1),
            Grado(id= 4, grado='Segundo', descripcion='Segundo de primaria', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15), colegio_id=1, materia_id=2),
            Grado(id= 5, grado='Tercero', descripcion='Tercero de primaria', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15), colegio_id=1, materia_id=3),
            Grado(id= 6, grado='Cuarto', descripcion='Cuarto de primaria', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15), colegio_id=1, materia_id=4),
            Grado(id= 7, grado='Quinto', descripcion='Quinto de primaria', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15), colegio_id=1, materia_id=5),
            Grado(id= 8, grado='Sexto', descripcion='Sexto de primaria', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15), colegio_id=1, materia_id=1),
            Grado(id= 9, grado='Septimo', descripcion='Septimo de primaria', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15), colegio_id=1, materia_id=2),
            Grado(id= 10, grado='Octavo', descripcion='Octavo de primaria', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15), colegio_id=1, materia_id=3),
            Grado(id= 11, grado='Noveno', descripcion='Noveno de primaria', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15), colegio_id=1, materia_id=4),
            Grado(id= 12, grado='Decimo', descripcion='Decimo de primaria', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15), colegio_id=1, materia_id=5),
            Grado(id= 13, grado='Once', descripcion='Once de primaria', created_at=datetime(2021, 4, 15), updated_at=datetime(2024, 4, 15), colegio_id=1, materia_id=1),
    ]
        db.session.bulk_save_objects(data)
        db.session.commit()

with app.app_context():
    db.create_all()

    insert_initial_values()