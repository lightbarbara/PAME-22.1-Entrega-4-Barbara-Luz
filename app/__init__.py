from flask import Flask
from .config import Config
from .extensions import db, migrate, mail, jwt
from app.encomenda.routes import encomenda_api
from app.funcionario.routes import funcionario_api
from app.loja.routes import loja_api
from app.produto.routes import produto_api
from app.cliente.routes import cliente_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    app.register_blueprint(encomenda_api)
    app.register_blueprint(funcionario_api)
    app.register_blueprint(loja_api)
    app.register_blueprint(produto_api)
    app.register_blueprint(cliente_api)
    return app
