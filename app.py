"""
    To run serve as development env:    

    $ export FLASK_APP="app.py:create_app()"
    $ export FLASK_ENV=development
    $ flask run
"""

from core.common.manage import create_app
from core.common.extensions import db

# Cover running server invoked by 'python app.py'
if __name__ == "__main__":
    app = create_app()
    app.run()