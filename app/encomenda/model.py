from app.extensions import db
from app.model import BaseModel

class Encomenda(BaseModel):
    __tablename__ = 'encomenda'

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.Integer, unique=True, nullable=False)
    categoria = db.Column(db.String(30))
    data = db.Column(db.String(20))
    realizada = db.Column(db.String(1), nullable=False)

    # cliente = db.Column(db.Integer, db.ForeignKey('cliente.id'))
    # produto = db.relationship('produto', secondary='encomendas_e_produtos', backref='produtos_das_entregas')

    def json(self):
        return {
            'id': self.id,
            'numero': self.numero,
            'categoria': self.categoria,
            'data': self.data,
            'realizada': self.realizada
        }

class EncomendasEProdutos(BaseModel):
    __tablename__ = 'encomendas_e_produtos'
    
    id = db.Column(db.Integer, primary_key=True)
    encomenda = db.Column(db.Integer, db.ForeignKey('encomenda.id'))
    produto = db.Column(db.Integer, db.ForeignKey('produto.id'))