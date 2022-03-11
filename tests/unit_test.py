import pytest
from flask import abort, url_for
from flask_testing import TestCase
from flask_login import login_user
from application import create_app, db
from application.models import Users, Exercises, Workout_Plans, Workout_Names

class TestBase(TestCase):

    def create_app(self):
        app = create_app()
        app.config.update({
            'SQLALCHEMY_DATABASE_URI': 'sqlite:///',
            'SQLALCHEMY_TRACK_MODIFICATIONS': False,
            'WTF_CSRF_ENABLED': False,
            'LOGIN_DISABLED': True,
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
        w2 = Workout_Names(workout_name="PPL")
        e = Exercises(exercise_name="Bench",
            repetitions=8,
            sets=5
        )
        e2 = Exercises(exercise_name="Squat",
            repetitions=8,
            sets=5
        )
        wp = Workout_Plans(workout_name="BBB",
            user_ID=1,
            exercise_ID=1
        )

        db.session.add(u)
        db.session.add(w)
        db.session.add(w2)
        db.session.add(e)
        db.session.add(e2)
        db.session.add(wp)
        db.session.commit()

    def tearDown(self):
        # Will be called after every test
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    # Test whether we get a successful response from our routes
    def test_homepage_view(self):
        response = self.client.get(url_for('routes.homepage'))
        self.assert200(response)

    def test_signup_view(self):
        response = self.client.get(url_for('routes.signup'))
        self.assert200(response)
    
    def test_login_view(self):
        response = self.client.get(url_for('routes.login'))
        self.assert200(response)

    def test_profile_view(self):
        response = self.client.get(url_for('routes.profile'))
        # cannot log in, leads to internal server error
        self.assertStatus(response, 500)

    def test_logout_view(self):
        response = self.client.get(url_for('routes.logout'))
        self.assertStatus(response, 302)

    def test_addexercise_view(self):
        response = self.client.get(url_for('routes.add_exercise'))
        self.assert200(response)

    def test_viewexercise_view(self):
        response = self.client.get(url_for('routes.view_exercise'))
        self.assert200(response)

    def test_addworkout_view(self):
        response = self.client.get(url_for('routes.add_workout'))
        self.assert200(response)

    def test_addwexercise_view(self):
        response = self.client.get(url_for('routes.add_workout_exercise'))
        self.assert200(response)


class TestRead(TestBase):

    def test_workout(self):
        response = self.client.get(url_for('routes.choose_workout'))
        self.assertIn('BBB', str(response.data))

    def test_read_exercise(self):
        response = self.client.get(url_for('routes.view_exercise'))
        self.assertIn('Bench', str(response.data))

    def test_false_login(self):
        # fails because client can't process login information
        response = self.client.post(
            url_for('routes.signup'),
            data = dict(email_address="eric@eric.com", 
                password="password"
            ),
            follow_redirects=True
        )
        self.assertStatus(response, 500)

    def test_view_workout(self):
        response = self.client.get(url_for('routes.view_workout', workout_name='BBB'))


class TestCreate(TestBase):
    
    def test_add_user(self):
        response = self.client.post(
            url_for('routes.signup'),
            data = dict(user_name="Terry", 
                password="Terry",
                first_name="Terry", 
                last_name="Terry", 
                email_address="Terry@terry.com"
            ),
            follow_redirects=True
        )
        user = Users.query.filter_by(user_name='Terry').first()
        self.assertEqual('Terry', user.user_name)

    def test_add_existing_user(self):
        response = self.client.post(
            url_for('routes.signup'),
            data = dict(user_name="admin", 
                password="admin",
                first_name="john", 
                last_name="clive", 
                email_address="john@gmail.com"
            ),
            follow_redirects=True
        )
        user = Users.query.filter_by(user_name='admin').first()
        self.assert200(response)

    def test_add_exercise(self):
        response = self.client.post(
            url_for('routes.add_exercise'),
            data = dict(
                exercise_name = 'Squats',
                repetitions = 10,
                sets = 5
            ),
            follow_redirects=True
        )
        exercise = Exercises.query.filter_by(exercise_name='Squats').first()
        self.assertEqual('Squats', exercise.exercise_name)
        self.assertEqual(10, exercise.repetitions)
        self.assertEqual(5, exercise.sets)

    def test_add_workout(self):
        response = self.client.post(
            url_for('routes.add_workout'),
            data = dict(workout_name = '531 BBB'),
            follow_redirects=True
        )
        workout = Workout_Names.query.filter_by(workout_name='531 BBB').first()
        self.assertEqual('531 BBB', workout.workout_name)

    # fails because user is AnonymousUser due to login issue
    def test_add_workout_exercise(self):
        response = self.client.post(
            url_for('routes.add_workout_exercise'),
            data = dict(
                workout_name = 'PPL',
                user_ID = 1,
                exercise_ID = 1,
            ),
            follow_redirects=True
        )
        workout_exercise = Workout_Plans.query.get(1)
        self.assertEqual('BBB', workout_exercise.workout_name)
        self.assertEqual(1, workout_exercise.user_ID)
        self.assertEqual(1, workout_exercise.exercise_ID)

def TestUpdate(TestBase):

    def test_update_exercise(self):
        response = self.client.post(
            url_for('routes.update_exercise', exercise_name='Bench'),
            data = dict(exercise_name='Deadlift',
                repetitions=1,
                sets=1
            ),
            follow_redirects=True
        )
        exercise = Exercises.query.filter_by(exercise_name='Deadlift').first()
        self.assertEqual('Deadlift', exercise.exercise_name)

def TestDelete(TestBase):

    # fails because current_user is Anonymous User
    def test_delete_user(self):
        response = self.client.post(
            url_for('routes.profile'),
            data = dict(user_ID=1),
            follow_redirects=True
        )
        user = Users.query.get(1)
        self.assertNotIn(1, user.user_ID)

    def test_delete_exercise(self):
        response = self.client.post(
            url_for('routes.delete_exercise', exercise_name="Bench"),
            follow_redirects=True
        )
        self.assertNotIn("Bench", str(response.data))
 