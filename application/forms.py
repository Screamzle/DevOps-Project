from flask_wtf import FlaskForm
from wtforms import StringField, DateTimeField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application import db
from application.models import Users, Exercises

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
