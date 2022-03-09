from application import create_app, db
from application.models import *

# with app.app_context():
db.drop_all()
db.create_all()