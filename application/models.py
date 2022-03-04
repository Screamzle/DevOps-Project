from flask_app import db
from datetime import datetime

# Join table for users and exercises
workout_plans = db.Table('workout_plans', db.Model.metadata,
    db.Column('exercise_ID', db.Integer, db.ForeignKey('exercises.exercise_ID')),
    db.Column('user_ID', db.Integer, db.ForeignKey('users.user_ID'))
)

# Table schema for users
class Users(db.Model):
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

# Table schema for exercises
class Exercises(db.Model):
    exercise_ID = db.Column(db.Integer, primary_key=True) # PK
    exercise_name = db.Column(db.String(50), nullable=False, unique=True) # Exercise name
    repetitions = db.Column(db.Integer, nullable=False) # Number of repetitions
    sets = db.Column(db.Integer, nullable=False) # Number of sets