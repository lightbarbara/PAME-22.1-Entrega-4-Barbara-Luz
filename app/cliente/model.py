from app.extensions import db
from app.model import BaseModel

class Cliente(BaseModel):
    __tablename__ = 'cliente'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(100), nullable=False)

    encomenda = db.relationship('Encomenda', backref='cliente')

    def json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'email': self.email,
            'endereco': self.endereco
        }