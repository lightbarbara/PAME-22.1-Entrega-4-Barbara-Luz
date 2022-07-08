from app.funcionario.controller import FuncionarioCreate, FuncionarioDetails, Login
from flask import Blueprint

funcionario_api = Blueprint('funcionario_api', __name__)

funcionario_api.add_url_rule('/registro_funcionario', view_func = FuncionarioCreate.as_view('registro_funcionario'), methods = ['POST', 'GET'])
funcionario_api.add_url_rule('/modifica_funcionario/<int:id>', view_func = FuncionarioDetails.as_view('modifica_funcionario'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])
funcionario_api.add_url_rule('/login', view_func = Login.as_view('login'), methods = ['POST'])