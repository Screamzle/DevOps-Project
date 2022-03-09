# Third party modules
import pytest

# First party modules
from application import create_app
from application.models import Users, Workout_Names, Workout_Plans, Exercises
from flask_testing import TestCase

@pytest.fixture
def client():
    app = create_app()

    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite://"

    db.init_app(app)