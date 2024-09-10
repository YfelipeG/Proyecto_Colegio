from app import db
from datetime import datetime


class User(db.Model):
    """
    Representa un estudiante.
    """
class Estudiante(db.Model):
    __tablename__ = 'estudiante'
    documento = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(45), nullable=False)
    apellidos = db.Column(db.String(45), nullable=False)
    telefono = db.Column(db.String(45))
    email = db.Column(db.String(45), unique=True)
    direccion = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    colegio_id = db.Column(db.Integer, db.ForeignKey('colegio.id'))
    grado_id = db.Column(db.Integer, db.ForeignKey('grado.id'))

    def __repr__(self):
        return f'<Estudiante {self.nombre} {self.apellidos}>'
