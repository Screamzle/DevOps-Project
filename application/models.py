from application import db
from datetime import datetime
from flask_login import UserMixin

# Table schema for users
class Users(UserMixin, db.Model):
    __tablename__ = 'users'
    user_ID = db.Column(db.Integer, primary_key=True) # PK
    user_name = db.Column(db.String(15), nullable=False, unique=True)# Username
    password = db.Column(db.String(100), nullable=False) # Password
    first_name = db.Column(db.String(50), nullable=False) # First name
    last_name = db.Column(db.String(50), nullable=False) # Last name
    email_address = db.Column(db.String(75), nullable=False, unique=True) # Email address
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow) # Date and time of account creation
    # creating relationship with Workout Plans
    workouts = db.relationship('Workout_Plans', backref='user')

    def get_id(self):
           return (self.user_ID)

class Workout_Names(db.Model):
    __tablename__ = 'workout_names'
    workout_name = db.Column(db.String(30), primary_key=True) # PK
    # creating relationship with Workout Plans
    workout_names = db.relationship('Workout_Plans', backref='name')

workout_exercises = db.Table('workout_exercises',
    db.Column('plan_id', db.Integer, db.ForeignKey('workout_plans.plan_id'), primary_key=True),
    db.Column('exercise_id', db.Integer, db.ForeignKey('exercises.exercise_ID'), primary_key=True)
)

# Table schema for workout_plans as association table
class Workout_Plans(db.Model):
    __tablename__ = 'workout_plans'
    plan_id = db.Column(db.Integer, primary_key=True) # PK
    workout_name = db.Column(db.String(30), db.ForeignKey('workout_names.workout_name'), nullable=False) # FK workout_names
    user_ID = db.Column(db.Integer, db.ForeignKey('users.user_ID'), nullable=False) # FK users
    exercise_ID = db.Column(db.Integer, db.ForeignKey('exercises.exercise_ID'), nullable=False) # FK exercises
    # creating relationship with exercises
    exercises = db.relationship('Exercises', secondary=workout_exercises, backref='workouts')

    def __init__(self, workout_name, user_ID, exercise_ID):
        self.workout_name = workout_name
        self.user_ID = user_ID
        self.exercise_ID = exercise_ID

    def __repr__(self):
        return 'Workout Plan: %s' % self.workout_name

# Table schema for exercises
class Exercises(db.Model):
    __tablename__ = 'exercises'
    exercise_ID = db.Column(db.Integer, primary_key=True) # PK
    exercise_name = db.Column(db.String(50), nullable=False, unique=True) # Exercise name
    repetitions = db.Column(db.Integer, nullable=False) # Number of repetitions
    sets = db.Column(db.Integer, nullable=False) # Number of sets

    def __init__(self, exercise_name, repetitions, sets):
        self.exercise_name = exercise_name
        self.repetitions = repetitions
        self.sets = sets

    def __repr__(self):
        return '<Exercise: %s>' % self.exercise_name