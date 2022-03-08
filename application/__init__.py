from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from jinja2 import Environment
import uuid
import os

db = SQLAlchemy()

# create Flask factory app, must be run with flask run on terminal instead
# must export FLASK_ENV=development, export FLASK_APP=application and export FLASK_RUN_HOST=0.0.0.0
def create_app(): 
    app = Flask(__name__)

    app.config['SECRET_KEY'] = str(uuid.uuid4()) # generating a random secret key at app startup
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # DATABASE_URI must be set in Jenkins/bash
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'login'
    login_manager.init_app(app)

    from application.models import Users, Exercises, Workout_Plans
    @login_manager.user_loader
    def load_user(user_id):
        return Users.query.get(int(user_id))

    # run FLASK_APP=application flask createdb in terminal to create tables
    # @app.cli.command()
    # def createdb():
    # with app.app_context(): # or with app.context when CLI won't work
    #     db.create_all()

    # run FLASK_APP=application flask dropdb in terminal to drop tables
    @app.cli.command()
    def dropdb():
        db.drop_all()

    jinja_env = Environment(extensions=['jinja2.ext.do'])
    app.jinja_env.add_extension('jinja2.ext.do')

    from application.routes import routes as routes_blueprint
    app.register_blueprint(routes_blueprint)

    return app