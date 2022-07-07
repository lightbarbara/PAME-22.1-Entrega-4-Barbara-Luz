from app.extensions import db
from app.model import BaseModel

class Funcionario(BaseModel):
    __tablename__ = 'funcionario'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=True)
    senha = db.Column(db.String(100), nullable=True)
    cargo = db.Column(db.String(30), nullable=True)
    cadastrado = db.Column(db.String(1), nullable=True)

    # local = db.Column(db.Integer, db.ForeignKey('loja.id'))

    def json(self):
        return {
            'id': self.id,
            'email': self.email,
            'cargo': self.cargo,
            'cadastrado': self.cadastrado
        }