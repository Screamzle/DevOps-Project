import pytest
from flask import abort, url_for
from flask_testing import TestCase
from application import create_app, db
from application.models import Users, Exercises, Workout_Plans, Workout_Names

class TestBase(TestCase):
    
    def create_app(self):
        app = create_app()
        app.config.update({
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///:memory:',
            'SQLALCHEMY_TRACK_MODIFICATIONS': False,
            'TESTING': True
        })
        db.init_app(app)
        return app

    def setUp(self):
        # Will be called before every test

        db.create_all()
        u = Users(user_name="admin",
            password="admin",
            first_name="john",
            last_name="clive",
            email_address="john@gmail.com",
        )
        w = Workout_Names(workout_name="BBB")
        wp = Workout_Plans(workout_name="BBB",
            user_ID=1,
            exercise_ID=1
        )
        e = Exercises(exercise_name="Bench",
            repetitions=8,
            sets=5
        )

        db.session.add(u)
        db.session.add(w)
        db.session.add(wp)
        db.session.add(e)
        db.session.commit()

        def tearDown(self):
            # Will be called after every test
            db.session.remove()
            db.drop_all()

class TestLogin(TestBase):

    def test_login_view(self):
        return 'test'

class TestViews(TestBase):

    # Test whether we get a successful response from our routes
    def test_signup_get(self):
        response = self.client.get(url_for('routes.signup'))
        self.assert200(response)

# class TestRead(TestBase):

#     test_read_user(self):


        
