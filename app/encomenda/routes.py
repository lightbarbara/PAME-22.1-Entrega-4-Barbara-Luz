from app.encomenda.controller import EncomendaCreate, EncomendaDetails
from flask import Blueprint

encomenda_api = Blueprint('encomenda_api', __name__)

encomenda_api.add_url_rule('/registro_encomenda', view_func = EncomendaCreate.as_view('registro_encomenda'), methods = ['POST', 'GET'])
encomenda_api.add_url_rule('/modifica_encomenda', view_func = EncomendaDetails.as_view('modifica_encomenda'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])