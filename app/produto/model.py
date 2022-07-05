from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

produto_api = Blueprint('produto_api', __name__)

class Produto(BaseModel):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    preco = db.Column(db.Integer)
    marca = db.Column(db.String(30))
    demanda = db.Column(db.String(10))

    local = db.Column(db.Integer, db.ForeignKey('local.id'))

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'preco': self.preco,
            'marca': self.marca,
            'demanda': self.demanda,
            'local': self.local
        }