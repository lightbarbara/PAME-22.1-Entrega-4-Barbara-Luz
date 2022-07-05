from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

encomenda_api = Blueprint('encomenda_api', __name__)

class Encomenda(BaseModel):
    __tablename__ = 'encomenda'

    id = db.Column(db.Integer, primary_key=True)
    categoria = db.Column(db.String(30))
    solicitante = db.Column(db.String(30))
    realizada = db.Column(db.String(1))
    produto = db.relationship('produto', secondary='encomendas_e_produtos', backref='produtos_das_entregas')

    def json(self):
        return {
            'id': self.id,
            'categoria': self.categoria,
            'solicitante': self.solicitante,
            'realizada': self.realizada
        }

class EncomendasEProdutos(BaseModel):
    __tablename__ = 'encomendas_e_produtos'
    
    id = db.Column(db.Integer, primary_key=True)
    encomenda = db.Column(db.Integer, db.ForeignKey('encomenda.id'))
    produto = db.Column(db.Integer, db.ForeignKey('produto.id'))