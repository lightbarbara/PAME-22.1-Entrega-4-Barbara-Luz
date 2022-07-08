from app.funcionario.model import Funcionario
from flask import request, jsonify
from flask.views import MethodView
import bcrypt
from flask_jwt_extended import create_access_token, verify_jwt_in_request, get_jwt_identity

class FuncionarioCreate(MethodView): # /registro
    def post(self):
        body = request.json # pegando do front

        id = body.get('id')
        email = body.get('email')
        senha = body.get('senha')
        senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
        cargo = body.get('cargo')
        cadastrado = body.get('cadastrado')
        loja_funcionario = body.get('loja_funcionario')

        if isinstance(email, str) and \
            isinstance(senha, str) and \
                isinstance(cargo, str) and \
                    isinstance(cadastrado, str) and \
                        isinstance(loja_funcionario, int):
            funcionario = Funcionario.query.filter_by(email=email).first()

            if funcionario:
                return {'code_status': 'Dados inválidos, funcionário já cadastrado'}, 400
            
            funcionario = Funcionario(email=email, senha=senha, cargo=cargo, cadastrado=cadastrado, loja_funcionario=loja_funcionario)
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
        loja_funcionario = body.get('loja_funcionario')

        if isinstance(email, str) and \
            isinstance(senha, str) and \
                isinstance(cargo, str) and \
                    isinstance(cadastrado, str) and \
                        isinstance(loja_funcionario, int):
            funcionario.email = email
            funcionario.senha = senha
            funcionario.cargo = cargo
            funcionario.cadastrado = cadastrado
            funcionario.loja_funcionario = loja_funcionario

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
        loja_funcionario = body.get('loja_funcionario', funcionario.loja_funcionario)

        if isinstance(email, str) and \
            isinstance(senha, str) and \
                isinstance(cargo, str) and \
                    isinstance(cadastrado, str) and \
                        isinstance(loja_funcionario, int):
            funcionario.email = email
            funcionario.senha = senha
            funcionario.cargo = cargo
            funcionario.cadastrado = cadastrado
            funcionario.loja_funcionario = loja_funcionario

            funcionario.update()

            return funcionario.json(), 200
    
    def delete(self, id):
        funcionario = Funcionario.query.get_or_404(id)
        funcionario.delete(funcionario)

        return funcionario.json()

class Login(MethodView):
    def post(self):
        body = request.json

        email = body.get('email')
        senha = body.get('senha')

        funcionario = Funcionario.query.filter_by(email=email).first()

        if funcionario and bcrypt.checkpw(senha.encode(), funcionario.senha.encode()):
            return {'token': create_access_token(funcionario.id, additional_claims={'usuario': 'logado'})}, 200
        return {'code_status': 'Email ou senha errados'}, 400
    