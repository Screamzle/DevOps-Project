from wtforms import StringField, DateTimeField, FloatField, PasswordField, BooleanField, SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_app import db, bcrypt
from flask_app.models import Users
from flask_login import current_user

# Create Account Form
class CreateAccountForm(FlaskForm):
    user_name = StringField('User Name: ',
        validators = [
            DataRequired(),
            Length(min = 3, max = 15)
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
    password = PasswordField('Password: ',
        validators = [
            DataRequired()
        ])
    confirm_password = PasswordField('Confirm Password: ',
        validators = [
            DataRequired(),
            EqualTo('password')
        ])
    submit = SubmitField('Create Account')

    def validate_username(self, user_name):
        user = Users.query.filter_by(user_name=user_name.data).first()

        if user:
            raise ValidationError('Username not available')

    def validate_email(self, email_address):
        user = Users.query.filter_by(email_address=email_address.data).first()

        if user:
            raise ValidationError('Email address already in use')

