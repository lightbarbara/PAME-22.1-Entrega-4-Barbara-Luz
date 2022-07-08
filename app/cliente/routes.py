from app.cliente.controller import ClienteCreate, ClienteDetails, Login
from flask import Blueprint

cliente_api = Blueprint('cliente_api', __name__)

cliente_api.add_url_rule('/registro_cliente', view_func = ClienteCreate.as_view('registro_cliente'), methods = ['POST', 'GET'])
cliente_api.add_url_rule('/modifica_cliente/<int:id>', view_func = ClienteDetails.as_view('modifica_cliente'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])
cliente_api.add_url_rule('/login', view_func = Login.as_view('login'), methods = ['POST'])
