from application import db
from datetime import datetime

# Table schema for users
class Users(db.Model):
    user_ID = db.Column(db.Integer, primary_key=True) # PK
    user_name = db.Column(db.String(15), nullable=False, unique=True)# Username
    password = db.Column(db.String(30), nullable=False) # Password
    first_name = db.Column(db.String(50), nullable=False) # First name
    last_name = db.Column(db.String(50), nullable=False) # Last name
    email_address = db.Column(db.String(75), nullable=False, unique=True) # Email address
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # Date and time of account creation
    # creating relationship with Workout Plans
    workout_plans = db.relationship('Workout_Plans', backref='user')

# Table schema for exercises
class Exercises(db.Model):
    exercise_ID = db.Column(db.Integer, primary_key=True) # PK
    exercise_name = db.Column(db.String(50), nullable=False, unique=True) # Exercise name
    repetitions = db.Column(db.Integer, nullable=False) # Number of repetitions
    sets = db.Column(db.Integer, nullable=False) # Number of sets
    # creating relationship with Workout Plans
    workout_plans = db.relationship('Workout_Plans', backref='exercise')

# Table schema for workout_plans as association table
class Workout_Plans(db.Model):
    plan_id = db.Column(db.Integer, primary_key=True)
    user_ID = db.Column('user_id', db.Integer, db.ForeignKey('users.user_ID'))
    exercise_ID = db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.exercise_ID'))
    workout_name = db.Column('Workout_Name', db.String(30))