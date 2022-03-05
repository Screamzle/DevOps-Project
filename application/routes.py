from application import db
from application.models import Users, Exercises, Workout_Plans
from application.forms import CreateAccountForm, LogInForm, UpdateAccountForm, DeleteAccountForm, ChangePWForm, CreateExerciseForm
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

routes = Blueprint('routes', __name__)

# create for homepage
@routes.route('/home')
@routes.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')

# create route for account creation
@routes.route('/signup', methods=['GET', 'POST'])
def signup():

    createform = CreateAccountForm()

    errors = False

    if request.method == 'POST':
        if createform.validate_on_submit():
            user = Users(user_name=createform.user_name.data, 
                password=generate_password_hash(createform.password.data, method='sha256'),
                first_name=createform.first_name.data, 
                last_name=createform.last_name.data, 
                email_address=createform.email_address.data
            )

            user_name = Users.query.filter_by(user_name=createform.user_name.data).first()
            email_address = Users.query.filter_by(email_address=createform.email_address.data).first()

            if user_name: # if username taken, flash error and redirect
                flash('Username already in use')
                errors = True
            if email_address: #if email taken, flash error and redirect
                flash('Email address already in use')
                errors = True
            
            if errors:
                return redirect(url_for('routes.signup'))
            else:
                db.session.add(user)
                db.session.commit()
                login_user(user)
        return redirect(url_for('routes.profile'))
    return render_template('signup.html', form=createform)

# create route to login
@routes.route('/login', methods=['GET', 'POST'])
def login():
    
    loginform = LogInForm()

    errors = False

    if request.method == 'POST':

        if loginform.validate_on_submit():
            login = Users(email_address=loginform.email_address.data, 
                password=loginform.password.data
            )
            
            user = Users.query.filter_by(email_address=login.email_address).first()

            # check if the user actually exists
            # take the user-supplied password, hash it, and compare it to the hashed password in the database
            if not user or not check_password_hash(user.password, login.password):
                flash('Please check your username/password and try again')
                errors = True

            if errors:
                return redirect(url_for('routes.login')) # if incorrect credentials, redirect back to login page
            
            login_user(user)
            return redirect(url_for('routes.profile')) # if correct, go to user profile

    return render_template('login.html', form=loginform)

# create route to view profile
@routes.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    
    # call forms
    updateform = UpdateAccountForm()
    changepwform = ChangePWForm()
    deleteform = DeleteAccountForm()

    if request.method == 'GET':
        updateform.user_name.data = current_user.user_name
        updateform.first_name.data = current_user.first_name
        updateform.last_name.data = current_user.last_name
        updateform.email_address.data = current_user.email_address

    elif request.method == 'POST':
        if updateform.validate_on_submit():
            current_user.user_name = updateform.user_name.data
            current_user.first_name = updateform.first_name.data
            current_user.last_name = updateform.last_name.data
            current_user.email_address = updateform.email_address.data
            db.session.commit()
            flash('Account has been updated!')
            return redirect(url_for('routes.profile'))

    if changepwform.validate_on_submit():
        user = current_user
        user.password = generate_password_hash(changepwform.password.data, method='sha256')
        db.session.add(user)
        db.session.commit()
        flash('Password has been updated!')
        return redirect(url_for('routes.profile'))
    
    if deleteform.validate_on_submit():
        user = Users.query.filter_by(user_ID=current_user.user_ID).first()
        logout_user()
        db.session.delete(user)
        db.session.commit()
        flash('Account has been deleted!')
        return redirect(url_for('routes.signup'))

    return render_template('profile.html', form=updateform, deleteform=deleteform, changepwform=changepwform, first_name=current_user.first_name, last_name=current_user.last_name)

# create route to logout
@routes.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('routes.login'))

# create route to add exercise
@routes.route('/add_exercise', methods=['GET', 'POST'])
@login_required
def add_exercise():
    
    form = CreateExerciseForm()

    if request.method == 'POST':
        if form.validate_on_submit():
            exercise = Exercises(exercise_name=form.exercise_name.data, 
                repetitions=form.repetitions.data,
                sets=form.sets.data
            )
            db.session.add(exercise)
            db.session.commit()
            flash('Exercise has been added')
            return redirect(url_for('routes.add_exercise'))
    return render_template('add_exercise.html', form=form)