from flask_app import db, login_manager
from flask_login import UserMixin
from datetime import datetime

# Join table for users and exercises
workout_plans = db.Table('workout_plans', db.Model.metadata,
    db.Column('exercise_ID', db.Integer, db.ForeignKey('exercises.exercise_ID')),
    db.Column('user_ID', db.Integer, db.ForeignKey('users.user_ID'))
)

# Table schema for users
class Users(db.Model, UserMixin):
    user_ID = db.Column(db.Integer, primary_key=True) # PK
    first_name = db.Column(db.String(50), nullable=False) # First name
    last_name = db.Column(db.String(50), nullable=False) # Last name
    email_address = db.Column(db.String(75), nullable=False, unique=True) # Email address
    user_name = db.Column(db.String(15), nullable=False, unique=True)# Username
    password = db.Column(db.String(30), nullable=False) # Password
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # Date and time of account creation

    # Define user relationship with exercises
    exercises = db.relationship('Exercises', cascade = 'delete', backref = 'author', lazy = True)
    workout_plans = db.relationship('Exercises', secondary = workout_plans, cascade = 'delete', backref = db.backref('workout_plans', lazy = 'dynamic'))

    # Getter function for 'load_user' function to get userID
    def get_id(self):
        return self.user_ID

    # Defines the format when querying the database
    def __repr__(self):
    	return ''.join([
            'User Name: ', self.user_name, '\r\n',
            'User ID: ', str(self.user_ID), '\r\n',
            'Email: ', self.email_address, '\r\n',
            'Name: ', self.first_name, ' ', self.last_name
	])

# Returns ID of user currently logged in
@login_manager.user_loader
def load_user(user_ID):
    return Users.query.get(int(user_ID))

# Table schema for exercises
class Exercises(db.Model):
    exercise_ID = db.Column(db.Integer, primary_key=True) # PK
    exercise_name = db.Column(db.String(50), nullable=False, unique=True) # Exercise name
    repetitions = db.Column(db.Integer, nullable=False) # Number of repetitions
    sets = db.Column(db.Integer, nullable=False) # Number of sets

    # Defines the format when querying the database
    def __repr__(self):
        return ''.join([
            'User ID: ', str(self.user_ID), '\r\n',
            'Exercise : ', self.exercise_name, '\r\n',
            'Number of Repetitions: ', str(self.repetitions), '\r\n',
            'Number of Sets: ', str(self.sets), '\r\n',
        ])