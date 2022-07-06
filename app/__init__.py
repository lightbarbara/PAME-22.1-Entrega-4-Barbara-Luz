from flask import Flask
from .config import Config
from .extensions import db, migrate
from app.encomenda.routes import encomenda_api
from app.funcionario.routes import funcionario_api
from app.local.routes import local_api
from app.produto.routes import produto_api

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    migrate.init_app(app, db)
    app.register_blueprint(encomenda_api)
    app.register_blueprint(funcionario_api)
    app.register_blueprint(local_api)
    app.register_blueprint(produto_api)
    return app
