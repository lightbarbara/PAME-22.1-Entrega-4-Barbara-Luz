from app.cliente.controller import ClienteCreate, ClienteDetails
from flask import Blueprint

cliente_api = Blueprint('cliente_api', __name__)

cliente_api.add_url_rule('/registro_cliente', view_func = ClienteCreate.as_view('registro_cliente'), methods = ['POST', 'GET'])
cliente_api.add_url_rule('/modifica_cliente', view_func = ClienteDetails.as_view('modifica_cliente'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])