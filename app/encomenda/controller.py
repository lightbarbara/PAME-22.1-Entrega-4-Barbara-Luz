from app.encomenda.model import Encomenda
from flask import request, jsonify
from flask.views import MethodView

class EncomendaCreate(MethodView):
    def post(self):
        body = request.json

        id = body.get('id')
        categoria = body.get('categoria')
        solicitante = body.get('solicitante')
        realizada = body.get('realizada')

        if isinstance(id, int) and \
            isinstance(categoria, str) and \
                isinstance(solicitante, str) and \
                    isinstance(realizada, str):
            encomenda = encomenda.query.filter_by(id=id).first()

            if encomenda:
                return {'code_status': 'Dados inválidos, encomenda já cadastrada'}, 400
            
            encomenda = Encomenda(categoria=categoria, solicitante=solicitante, realizada=realizada)