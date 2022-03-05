from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateTimeField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from application import db
from application.models import Users, Exercises
from flask_login import current_user

# Create Account Form
class CreateAccountForm(FlaskForm):
    user_name = StringField('User Name: ',
        validators = [
            DataRequired(),
            Length(min = 3, max = 15)
        ])
    password = PasswordField('Password: ',
        validators = [
            DataRequired()
        ])
    first_name = StringField('First Name: ',
        validators = [
            DataRequired(),
            Length(min = 3, max = 50)
            ])
    last_name = StringField('Last Name: ',
        validators = [
            DataRequired(),
            Length(min = 2, max = 50)
            ])
    email_address = StringField('Email Address: ',
        validators = [
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Create Account')

# LogIn Form
class LogInForm(FlaskForm):
    email_address = StringField('Email Address: ',
        validators = [
            DataRequired(),
            Email()
        ])
    password = PasswordField('Password: ',
        validators = [
            DataRequired()
        ])
    submit = SubmitField('Sign in')

# Update Account Form
class UpdateAccountForm(FlaskForm):
    user_name = StringField('User Name: ',
        validators = [
            DataRequired(),
            Length(min = 3, max = 15),
        ])
    first_name = StringField('First Name: ',
        validators = [
            DataRequired(),
            Length(min = 3, max = 50)
            ])
    last_name = StringField('Last Name: ',
        validators = [
            DataRequired(),
            Length(min = 2, max = 50)
            ])
    email_address = StringField('Email Address: ',
        validators = [
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update Account Details')

# Delete Account Form
class DeleteAccountForm(FlaskForm):
    delete = SubmitField('Delete Account')

# Change Password Form
class ChangePWForm(FlaskForm):
    password = PasswordField('Password: ',
        validators = [
            DataRequired()
        ])
    change = SubmitField('Change Password')

# Create Exercise Form
class CreateExerciseForm(FlaskForm):
    exercise_name = StringField('Exercise Name: ',
        validators = [
            DataRequired(),
            Length(min = 3, max = 50)
        ])
    repetitions = IntegerField('Number of repetitions: ',
        validators = [
            DataRequired(),
            NumberRange(min=1, max=25, message="Please enter a number between 1 and 25")
        ])
    sets = IntegerField('Number of sets: ',
        validators = [
            DataRequired(),
            NumberRange(min=1, max=15, message="Please enter a number between 1 and 15")
        ])
    submit = SubmitField('Add Exercise')