from app.extensions import db
from app.model import BaseModel

class Local(BaseModel):
    __tablename__ = 'local'

    id = db.Column(db.Integer, primary_key=True)
    espaco = db.Column(db.String(100), unique=True)
    area = db.Column(db.Float)

    # produtos = db.relationship('produto', backref='local')
    # funcionarios = db.relationship('funcionario', backref='local')

    def json(self):
        return {
            'id': self.id,
            'espaco': self.espaco,
            'area': self.area,
        }