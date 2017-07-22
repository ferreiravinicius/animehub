#Enable debug env
DEBUG = True

#Define application root directory absolute path for sqlite
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

#Setup Database (SQLAlchemy)
# SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'app.db')
SQLALCHEMY_DATABASE_URI = 'mysql://flask:flask123@localhost/animehub' #pip install mysqlclient
DATABASE_CONNECT_OPTIONS = {}
SQLALCHEMY_TRACK_MODIFICATIONS = True

#Setup Application Threads (checkup)
THREADS_PER_PAGE = 2

#Setup WTForms CRSF token
CSRF_ENABLED = True
CSRF_SESSION_KEY = 'senha_demoniaca'

#App secret key for signing cookies
SECRET_KEY = 'secret'

EXPLAIN_TEMPLATE_LOADING = False