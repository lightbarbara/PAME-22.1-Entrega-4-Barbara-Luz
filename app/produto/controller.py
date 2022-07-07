from app.produto.model import Produto
from flask import request, jsonify
from flask.views import MethodView

class ProdutoCreate(MethodView): # /registro
    def post(self):
        body = request.json # pegando do front

        id = body.get('id')
        nome = body.get('nome')
        preco = body.get('preco')
        marca = body.get('marca')
        tipo = body.get('tipo')
        demanda = body.get('demanda')
        quantidade = body.get('quantidade')
        loja = body.get('loja')

        if isinstance(nome, str) and \
            isinstance(preco, float) and \
                isinstance(marca, str) and \
                    isinstance(tipo, str) and \
                        isinstance(demanda, int) and \
                            isinstance(quantidade, int) and \
                                isinstance(loja, int):
            produto = Produto.query.filter_by(nome=nome).first()

            if produto:
                return {'code_status': 'Dados inválidos, produto já cadastrado'}, 400
            
            produto = Produto(nome=nome, preco=preco, marca=marca, tipo=tipo, demanda=demanda, quantidade=quantidade, loja=loja)
            produto.save()
            return produto.json(), 200
    
    def get(self):
        produtos = Produto.query.all()
        return jsonify([produto.json() for produto in produtos]), 200
    
class ProdutoDetails(MethodView):
    def get(self, id):
        produto = Produto.query.get_or_404(id)
        return produto.json()
    
    def put(self, id):
        body = request.json()
        produto = Produto.query.get_or_404(id)

        nome = body.get('nome')
        preco = body.get('preco')
        marca = body.get('marca')
        tipo = body.get('tipo')
        demanda = body.get('demanda')
        quantidade = body.get('quantidade')
        loja = body.get('loja')

        if isinstance(nome, str) and \
            isinstance(preco, float) and \
                isinstance(marca, str) and \
                    isinstance(tipo, str) and \
                        isinstance(demanda, int) and \
                            isinstance(quantidade, int) and \
                                isinstance(loja, int):
            produto.nome = nome
            produto.preco = preco
            produto.marca = marca
            produto.tipo = tipo
            produto.demanda = demanda
            produto.quantidade = quantidade
            produto.loja = loja

            produto.update()

            return produto.json(), 200
        
        else:
            return {'code_status': 'Dados inválidos'}, 400
    
    def patch(self, id):
        body = request.json()
        produto = Produto.query.get_or_404(id)

        nome = body.get('nome', produto.nome)
        preco = body.get('preco', produto.preco)
        marca = body.get('marca', produto.marca)
        tipo = body.get('tipo', produto.tipo)
        demanda = body.get('demanda', produto.demanda)
        quantidade = body.get('quantidade', produto.quantidade)
        loja = body.get('loja', produto.loja)

        if isinstance(nome, str) and \
            isinstance(preco, float) and \
                isinstance(marca, str) and \
                    isinstance(tipo, str) and \
                        isinstance(demanda, int) and \
                            isinstance(quantidade, int) and \
                                isinstance(loja, int):
            produto.nome = nome
            produto.preco = preco
            produto.marca = marca
            produto.tipo = tipo
            produto.demanda = demanda
            produto.quantidade = quantidade
            produto.loja = loja

            produto.update()

            return produto.json(), 200
    
    def delete(self, id):
        produto = Produto.query.get_or_404(id)
        produto.delete(produto)

        return produto.json()