from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import uuid
import os

db = SQLAlchemy()

# create Flask factory app, must be run with flask run on terminal instead
# must export FLASK_ENV=development and export FLASK_APP=application
def create_app(): 
    app = Flask(__name__)

    app.config['SECRET_KEY'] = str(uuid.uuid4()) # generating a random secret key at app startup
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # DATABASE_URI must be set in Jenkins/bash
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    from application.models import Users
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    from application.routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app