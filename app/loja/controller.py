from app.loja.model import Loja
from flask import request, jsonify
from flask.views import MethodView

class LojaCreate(MethodView): # /registro
    def post(self):
        body = request.json # pegando do front

        id = body.get('id')
        espaco = body.get('espaco')
        area = body.get('area')

        if isinstance(espaco, str) and \
            isinstance(area, float):
            loja = Loja.query.filter_by(espaco=espaco).first()

            if loja:
                return {'code_status': 'Dados inválidos, loja já cadastrada'}, 400
            
            loja = Loja(espaco=espaco, area=area)
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

        espaco = body.get('espaco')
        area = body.get('area')

        if isinstance(espaco, str) and \
            isinstance(area, float):
            loja.espaco = espaco
            loja.area = area

            loja.update()

            return loja.json(), 200
        
        else:
            return {'code_status': 'Dados inválidos'}, 400
    
    def patch(self, id):
        body = request.json()
        loja = Loja.query.get_or_404(id)

        espaco = body.get('espaco', loja.espaco)
        area = body.get('area', loja.area)

        if isinstance(espaco, str) and \
            isinstance(area, float):
            loja.espaco = espaco
            loja.area = area
            
            loja.update()

            return loja.json(), 200
    
    def delete(self, id):
        loja = Loja.query.get_or_404(id)
        loja.delete(loja)

        return loja.json()