from app.local.model import Local
from flask import request, jsonify
from flask.views import MethodView

class LocalCreate(MethodView): # /registro
    def post(self):
        body = request.json # pegando do front

        id = body.get('id')
        espaco = body.get('espaco')
        area = body.get('area')

        if isinstance(espaco, str) and \
            isinstance(area, float):
            local = Local.query.filter_by(espaco=espaco).first()

            if local:
                return {'code_status': 'Dados inválidos, local já cadastrado'}, 400
            
            local = Local(espaco=espaco, area=area)
            local.save()
            return local.json(), 200
    
    def get(self):
        locais = Local.query.all()
        return jsonify([local.json() for local in locais]), 200
    
class LocalDetails(MethodView):
    def get(self, id):
        local = Local.query.get_or_404(id)
        return local.json()
    
    def put(self, id):
        body = request.json()
        local = Local.query.get_or_404(id)

        espaco = body.get('espaco')
        area = body.get('area')

        if isinstance(espaco, str) and \
            isinstance(area, float):
            local.espaco = espaco
            local.area = area

            local.update()

            return local.json(), 200
        
        else:
            return {'code_status': 'Dados inválidos'}, 400
    
    def patch(self, id):
        body = request.json()
        local = Local.query.get_or_404(id)

        espaco = body.get('espaco', local.espaco)
        area = body.get('area', local.area)

        if isinstance(espaco, str) and \
            isinstance(area, float):
            local.espaco = espaco
            local.area = area
            
            local.update()

            return local.json(), 200
    
    def delete(self, id):
        local = Local.query.get_or_404(id)
        local.delete(local)

        return local.json()