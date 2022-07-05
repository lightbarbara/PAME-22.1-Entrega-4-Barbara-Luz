from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

funcionario_api = Blueprint('funcionario_api', __name__)

class Funcionario(BaseModel):
    __tablename__ = 'funcionario'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    tipo = db.Column(db.String(30))
    cadastrado = db.Column(db.String(1))

    local = db.Column(db.Integer, db.ForeignKey('local.id'))

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'tipo': self.tipo,
            'cadastrado': self.cadastrado
        }