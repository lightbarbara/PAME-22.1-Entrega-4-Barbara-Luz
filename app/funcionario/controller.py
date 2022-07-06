from app.funcionario.model import Funcionario
from flask import request, jsonify
from flask.views import MethodView

class FuncionarioCreate(MethodView): # /registro
    def post(self):
        body = request.json # pegando do front

        id = body.get('id')
        nome = body.get('nome')
        cargo = body.get('cargo')
        cadastrado = body.get('cadastrado')

        if isinstance(nome, str) and \
            isinstance(cargo, str) and \
                isinstance(cadastrado, str):
            funcionario = Funcionario.query.filter_by(nome=nome).first()

            if funcionario:
                return {'code_status': 'Dados inválidos, funcionário já cadastrado'}, 400
            
            funcionario = Funcionario(nome=nome, cargo=cargo, cadastrado=cadastrado)
            funcionario.save()
            return funcionario.json(), 200
    
    def get(self):
        funcionarios = Funcionario.query.all()
        return jsonify([funcionario.json() for funcionario in funcionarios]), 200
    
class FuncionarioDetails(MethodView):
    def get(self, id):
        funcionario = Funcionario.query.get_or_404(id)
        return funcionario.json()
    
    def put(self, id):
        body = request.json()
        funcionario = Funcionario.query.get_or_404(id)

        nome = body.get('nome')
        cargo = body.get('cargo')
        cadastrado = body.get('cadastrado')

        if isinstance(nome, str) and \
            isinstance(cargo, str) and \
                isinstance(cadastrado, str):
            funcionario.nome = nome
            funcionario.cargo = cargo
            funcionario.cadastrado = cadastrado

            funcionario.update()

            return funcionario.json(), 200
        
        else:
            return {'code_status': 'Dados inválidos'}, 400
    
    def patch(self, id):
        body = request.json()
        funcionario = Funcionario.query.get_or_404(id)

        nome = body.get('nome', funcionario.nome)
        cargo = body.get('cargo', funcionario.cargo)
        cadastrado = body.get('cadastrado', funcionario.cadastrado)

        if isinstance(nome, str) and \
            isinstance(cargo, str) and \
                isinstance(cadastrado, str):
            funcionario.nome = nome
            funcionario.cargo = cargo
            funcionario.cadastrado = cadastrado

            funcionario.update()

            return funcionario.json(), 200
    
    def delete(self, id):
        funcionario = Funcionario.query.get_or_404(id)
        funcionario.delete(funcionario)

        return funcionario.json()