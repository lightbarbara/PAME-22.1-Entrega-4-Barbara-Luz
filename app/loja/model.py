from app.extensions import db
from app.model import BaseModel

class Loja(BaseModel):
    __tablename__ = 'loja'

    id = db.Column(db.Integer, primary_key=True)
    local = db.Column(db.String(100), unique=True, nullable=False)
    area_estoque = db.Column(db.Float)

    produtos = db.relationship('Produto', backref='loja')
    funcionarios = db.relationship('Funcionario', backref='loja')

    def json(self):
        return {
            'id': self.id,
            'local': self.local,
            'area_estoque': self.area_estoque,
        }