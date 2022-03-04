from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_app import db
from flask_app.models import Users, Exercises

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

    def check_username(self, user_name):


    def check_email(self, email_address):
