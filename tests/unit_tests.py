import pytest
from flask import abort, url_for
from flask_testing import TestCase
from application import create_app, db
from application.models import Users, Exercises, Workout_Plans, Workout_Names


class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        app.config.update(
            SQLALCHEMY_DATABASE_URI='sqlite:///',
            DEBUG=True,
            WTF_CSRF_ENABLED=False
        )
        return app

    def setUp(self):
        db.create_all()
        u = Users(user_name="admin",
            password="admin",
            first_name="john",
            last_name="clive",
            email_address=john@gmail.com,
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
        db.drop_all()

class TestLogin(TestBase):

    def test_login_view(self):
        '''
        Test that login is accessible without being logged in
        '''
        response = self.client.get(url_for('signup'))
        self.assertEqual(response.status_code, 200)
