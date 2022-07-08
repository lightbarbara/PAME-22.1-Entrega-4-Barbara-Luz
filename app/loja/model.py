from app.extensions import db
from app.model import BaseModel

class Loja(BaseModel):
    __tablename__ = 'loja'

    id = db.Column(db.Integer, primary_key=True)
    espaco = db.Column(db.String(100), unique=True, nullable=False)
    area = db.Column(db.Float)

    produtos = db.relationship('Produto', backref='loja')
    funcionarios = db.relationship('Funcionario', backref='loja')

    def json(self):
        return {
            'id': self.id,
            'espaco': self.espaco,
            'area': self.area,
        }