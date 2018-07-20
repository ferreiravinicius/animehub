from flask import Flask
from .extensions import db

def create_app(name='boilerplate', 
               config='core.common.config.DevelopmentConfig'):
    """Create the Flask app instance"""
    app = Flask(name)
    app.config.from_object(config)

    configure_extensions(app)
    configure_blueprints(app)
    configure_cli(app)

    return app

def configure_blueprints(app):
    """Register application blueprints"""
    from ..modules.main.views import main as bp_main
    app.register_blueprint(bp_main)

    #from .pet.views import pet as bp_pet
    #app.register_blueprint(bp_pet, url_prefix="/pet")

def configure_extensions(app):
    """Initialize dependencies and extensions"""

    #Database ORM
    db.init_app(app)

def configure_cli(app):
    """Configure custom CLI commands"""
    pass
