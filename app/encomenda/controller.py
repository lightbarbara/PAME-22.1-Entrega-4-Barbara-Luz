from app.encomenda.model import Encomenda
from flask import request, jsonify
from flask.views import MethodView

class EncomendaCreate(MethodView): # /registro
    def post(self):
        body = request.json # pegando do front

        id = body.get('id')
        numero = body.get('numero')
        categoria = body.get('categoria')
        cliente = body.get('cliente')
        data = body.get('data')
        realizada = body.get('realizada')

        if isinstance(numero, int) and \
            isinstance(categoria, str) and \
                isinstance(cliente, str) and \
                    isinstance(data, str) and \
                        isinstance(realizada, str):
            encomenda = Encomenda.query.filter_by(numero=numero).first()

            if encomenda:
                return {'code_status': 'Dados inválidos, encomenda já cadastrada'}, 400
            
            encomenda = Encomenda(numero=numero, categoria=categoria, cliente=cliente, data=data, realizada=realizada)
            encomenda.save()
            return encomenda.json(), 200
    
    def get(self):
        encomendas = Encomenda.query.all()
        return jsonify([encomenda.json() for encomenda in encomendas]), 200
    
class EncomendaDetails(MethodView):
    def get(self, id):
        encomenda = Encomenda.query.get_or_404(id)
        return encomenda.json()
    
    def put(self, id):
        body = request.json()
        encomenda = Encomenda.query.get_or_404(id)

        numero = body.get('numero')
        categoria = body.get('categoria')
        cliente = body.get('cliente')
        data = body.get('data')
        realizada = body.get('realizada')

        if isinstance(numero, int) and \
            isinstance(categoria, str) and \
                isinstance(cliente, str) and \
                    isinstance(data, str) and \
                        isinstance(realizada, str):
            encomenda.numero = numero
            encomenda.categoria = categoria
            encomenda.cliente = cliente
            encomenda.data = data
            encomenda.realizada = realizada

            encomenda.update()

            return encomenda.json(), 200
        
        else:
            return {'code_status': 'Dados inválidos'}, 400
    
    def patch(self, id):
        body = request.json()
        encomenda = Encomenda.query.get_or_404(id)

        numero = body.get('numero', encomenda.numero)
        categoria = body.get('categoria', encomenda.categoria)
        cliente = body.get('cliente', encomenda.cliente)
        data = body.get('data', encomenda.data)
        realizada = body.get('realizada', encomenda.realizada)

        if isinstance(numero, int) and \
            isinstance(categoria, str) and \
                isinstance(cliente, str) and \
                    isinstance(data, str) and \
                        isinstance(realizada, str):
            encomenda.numero = numero
            encomenda.categoria = categoria
            encomenda.cliente = cliente
            encomenda.data = data
            encomenda.realizada = realizada

            encomenda.update()

            return encomenda.json(), 200
    
    def delete(self, id):
        encomenda = Encomenda.query.get_or_404(id)
        encomenda.delete(encomenda)

        return encomenda.json()