import os

class Config():
    # Setup Flask
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'secret'
    
    # Setup Database (SQLAlchemy)
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
    # May need apt install mysqlclient-dev and apt install python3.6-dev
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@localhost/stordev' #pip install mysqlclient 
    DATABASE_CONNECT_OPTIONS = {}
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    EXPLAIN_TEMPLATE_LOADING = True

class TestingConfig(Config):
    TESTING = True