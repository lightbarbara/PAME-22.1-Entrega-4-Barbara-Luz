from app.funcionario.controller import FuncionarioCreate, FuncionarioDetails
from flask import Blueprint

funcionario_api = Blueprint('funcionario_api', __name__)

funcionario_api.add_url_rule('/registro_funcionario', view_func = FuncionarioCreate.as_view('registro_funcionario'), methods = ['POST', 'GET'])
funcionario_api.add_url_rule('/modifica_funcionario', view_func = FuncionarioDetails.as_view('modifica_funcionario'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])