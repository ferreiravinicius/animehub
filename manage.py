from animehub.core import create_app
from animehub.extensions import db

app = create_app()

with app.app_context():
    db.create_all()

app.run()