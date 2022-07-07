from app.loja.controller import LojaCreate, LojaDetails
from flask import Blueprint

loja_api = Blueprint('loja_api', __name__)

loja_api.add_url_rule('/registro_loja', view_func = LojaCreate.as_view('registro_loja'), methods = ['POST', 'GET'])
loja_api.add_url_rule('/modifica_loja', view_func = LojaDetails.as_view('modifica_loja'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])