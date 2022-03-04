from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import uuid
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = str(uuid.uuid4()) # generating a random secret key at app startup
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI") # DATABASE_URI must be set in Jenkins/bash
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes