from flask import Flask
from .extensions import db

def create_app(config='animehub.configs.dev'):
    """Cria uma instancia do app e inicializa extensões e Blueprints""" 
      
    app = Flask("animehub")
    app.config.from_object(config)

    #Dependencias
    configure_blueprints(app)
    configure_extensions(app)

    return app

def configure_blueprints(app):
    """Registra os Blueprints"""

    from .main.views import main as bp_main
    app.register_blueprint(bp_main)

    #from .pet.views import pet as bp_pet
    #app.register_blueprint(bp_pet, url_prefix="/pet")

def configure_extensions(app):
    "Inicializa extensões e dependencias"

    db.init_app(app)
