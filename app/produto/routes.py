from app.produto.controller import ProdutoCreate, ProdutoDetails
from flask import Blueprint

produto_api = Blueprint('produto_api', __name__)

produto_api.add_url_rule('/registro_produto', view_func = ProdutoCreate.as_view('registro_produto'), methods = ['POST', 'GET'])
produto_api.add_url_rule('/modifica_produto/<int:id>', view_func = ProdutoDetails.as_view('modifica_produto'), methods = ['GET', 'PUT', 'PATCH', 'DELETE'])