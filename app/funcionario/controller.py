from app.funcionario.model import Funcionario
from flask import request, jsonify
from flask.views import MethodView
import bcrypt

class FuncionarioCreate(MethodView): # /registro
    def post(self):
        body = request.json # pegando do front

        id = body.get('id')
        email = body.get('email')
        senha = body.get('senha')
        senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
        cargo = body.get('cargo')
        cadastrado = body.get('cadastrado')
        loja = body.get('loja')

        if isinstance(email, str) and \
            isinstance(senha, str) and \
                isinstance(cargo, str) and \
                    isinstance(cadastrado, str) and \
                        isinstance(loja, int):
            funcionario = Funcionario.query.filter_by(email=email).first()

            if funcionario:
                return {'code_status': 'Dados inválidos, funcionário já cadastrado'}, 400
            
            funcionario = Funcionario(email=email, senha=senha, cargo=cargo, cadastrado=cadastrado, loja=loja)
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

        email = body.get('email')
        senha = body.get('senha')
        cargo = body.get('cargo')
        cadastrado = body.get('cadastrado')
        loja = body.get('loja')

        if isinstance(email, str) and \
            isinstance(senha, str) and \
                isinstance(cargo, str) and \
                    isinstance(cadastrado, str) and \
                        isinstance(loja, int):
            funcionario.email = email
            funcionario.senha = senha
            funcionario.cargo = cargo
            funcionario.cadastrado = cadastrado
            funcionario.loja = loja

            funcionario.update()

            return funcionario.json(), 200
        
        else:
            return {'code_status': 'Dados inválidos'}, 400
    
    def patch(self, id):
        body = request.json()
        funcionario = Funcionario.query.get_or_404(id)

        email = body.get('email', funcionario.email)
        senha = body.get('senha', funcionario.senha)
        cargo = body.get('cargo', funcionario.cargo)
        cadastrado = body.get('cadastrado', funcionario.cadastrado)
        loja = body.get('loja', funcionario.loja)

        if isinstance(email, str) and \
            isinstance(senha, str) and \
                isinstance(cargo, str) and \
                    isinstance(cadastrado, str) and \
                        isinstance(loja, int):
            funcionario.email = email
            funcionario.senha = senha
            funcionario.cargo = cargo
            funcionario.cadastrado = cadastrado
            funcionario.loja = loja

            funcionario.update()

            return funcionario.json(), 200
    
    def delete(self, id):
        funcionario = Funcionario.query.get_or_404(id)
        funcionario.delete(funcionario)

        return funcionario.json()

# class Login(MethodView):
    