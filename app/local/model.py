from app.extensions import db
from app.model import BaseModel
from flask import Blueprint

local_api = Blueprint('local_api', __name__)

class Local(BaseModel):
    __tablename__ = 'local'

    id = db.Column(db.Integer, primary_key=True)
    espaco = db.Column(db.String(100))
    area = db.Column(db.Float)

    produtos = db.relationship('produto', backref='local')
    funcionarios = db.relationship('funcionario', backref='local')

    def json(self):
        return {
            'id': self.id,
            'espaco': self.espaco,
            'area': self.area,
        }