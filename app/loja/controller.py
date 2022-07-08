from app.loja.model import Loja
from flask import request, jsonify
from flask.views import MethodView

class LojaCreate(MethodView): # /registro
    def post(self):
        body = request.json # pegando do front

        id = body.get('id')
        local = body.get('local')
        area_estoque = body.get('area_estoque')

        if isinstance(local, str) and \
            isinstance(area_estoque, float):
            loja = Loja.query.filter_by(local=local).first()

            if loja:
                return {'code_status': 'Dados inválidos, loja já cadastrada'}, 400
            
            loja = Loja(local=local, area_estoque=area_estoque)
            loja.save()
            return loja.json(), 200
    
    def get(self):
        lojas = Loja.query.all()
        return jsonify([loja.json() for loja in lojas]), 200
    
class LojaDetails(MethodView):
    def get(self, id):
        loja = Loja.query.get_or_404(id)
        return loja.json()
    
    def put(self, id):
        body = request.json()
        loja = Loja.query.get_or_404(id)

        local = body.get('local')
        area_estoque = body.get('area_estoque')

        if isinstance(local, str) and \
            isinstance(area_estoque, float):
            loja.local = local
            loja.area_estoque = area_estoque

            loja.update()

            return loja.json(), 200
        
        else:
            return {'code_status': 'Dados inválidos'}, 400
    
    def patch(self, id):
        body = request.json()
        loja = Loja.query.get_or_404(id)

        local = body.get('local', loja.local)
        area_estoque = body.get('area_estoque', loja.area_estoque)

        if isinstance(local, str) and \
            isinstance(area_estoque, float):
            loja.local = local
            loja.area_estoque = area_estoque
            
            loja.update()

            return loja.json(), 200
    
    def delete(self, id):
        loja = Loja.query.get_or_404(id)
        loja.delete(loja)

        return loja.json()