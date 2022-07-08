from app.extensions import db
from app.model import BaseModel

class Produto(BaseModel):
    __tablename__ = 'produto'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    marca = db.Column(db.String(30))
    tipo = db.Column(db.String(30))
    demanda = db.Column(db.Integer)
    quantidade = db.Column(db.Integer, nullable=False)

    loja_produto = db.Column(db.Integer, db.ForeignKey('loja.id'))

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'preco': self.preco,
            'marca': self.marca,
            'demanda': self.demanda,
            'quantidade': self.quantidade,
            'loja': self.loja
        }