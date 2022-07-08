from app.cliente.model import Cliente
from flask import render_template, request, jsonify
from flask.views import MethodView
from flask_mail import Message
from app.extensions import mail
import bcrypt
from flask_jwt_extended import create_access_token, verify_jwt_in_request, get_jwt_identity

class ClienteCreate(MethodView): # /registro
    def post(self):
        body = request.json # pegando do front

        id = body.get('id')
        nome = body.get('nome')
        email = body.get('email')
        senha = body.get('senha')
        senha = bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()
        endereco = body.get('endereco')

        if isinstance(nome, str) and \
            isinstance(email, str) and \
                isinstance(senha, str) and \
                    isinstance(endereco, str):
            cliente = Cliente.query.filter_by(email=email).first()

            if cliente:
                return {'code_status': 'Dados inválidos, cliente já cadastrado'}, 400
            
            cliente = Cliente(nome=nome, email=email, senha=senha, endereco=endereco)
            cliente.save()

            mensagem = Message(sender='barbaraluz@eq.ufrj.br', recipients = [email],
            subject='Cadastro completo', html = render_template('email.html', nome=nome))
            mail.send(mensagem)

            return cliente.json(), 200
    
    def get(self):
        clientes = Cliente.query.all()
        return jsonify([cliente.json() for cliente in clientes]), 200
    
class ClienteDetails(MethodView):

    def get(self, id):
        verify_jwt_in_request()
        if id == get_jwt_identity():
            cliente = Cliente.query.get_or_404(id)
            return cliente.json()
        return {'code_status': 'O id passado é inválido'}, 400
    
    def put(self, id):
        body = request.json()
        cliente = Cliente.query.get_or_404(id)

        nome = body.get('nome')
        email = body.get('email')
        senha = body.get('senha')
        endereco = body.get('endereco')

        if isinstance(nome, str) and \
            isinstance(email, str) and \
                isinstance(senha, str) and \
                    isinstance(endereco, str):
            cliente.nome = nome
            cliente.email = email
            cliente.senha = senha
            cliente.endereco = endereco

            cliente.update()

            return cliente.json(), 200
        
        else:
            return {'code_status': 'Dados inválidos'}, 400
    
    def patch(self, id):
        body = request.json()
        cliente = Cliente.query.get_or_404(id)

        nome = body.get('nome', cliente.nome)
        email = body.get('email', cliente.email)
        senha = body.get('senha', cliente.senha)
        endereco = body.get('endereco', cliente.endereco)

        if isinstance(nome, str) and \
            isinstance(email, str) and \
                isinstance(senha, str) and \
                    isinstance(endereco, str):
            cliente.nome = nome
            cliente.email = email
            cliente.senha = senha
            cliente.endereco = endereco

            cliente.update()

            return cliente.json(), 200
    
    def delete(self, id):
        cliente = Cliente.query.get_or_404(id)
        cliente.delete(cliente)

        return cliente.json()

class Login(MethodView):
    def post(self):
        body = request.json

        email = body.get('email')
        senha = body.get('senha')

        cliente = Cliente.query.filter_by(email=email).first()

        if cliente and bcrypt.checkpw(senha.encode(), cliente.senha.encode()):
            return {'token': create_access_token(cliente.id)}, 200
        return {'code_status': 'Email ou senha errados'}, 400