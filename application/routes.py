from application import app, db
from application.models import Users, Exercises, Workout_Plans
from application.forms import CreateAccountForm, LogInForm
from flask import render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash

# create for homepage
@app.route('/home')
@app.route('/', methods=['GET', 'POST'])
def homepage():
    return render_template('homepage.html')

# create route for account creation
@app.route('/signup', methods=['GET', 'POST'])
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
                return redirect(url_for('signup'))

            db.session.add(user)
            db.session.commit()
        return redirect(url_for('profile'))
    return render_template('signup.html', form=createform)

# create route to login
@app.route('/login', methods=['GET', 'POST'])
def login():
    
    loginform = LogInForm()

    errors = False

    if request.method == 'POST':
        if loginform.validate_on_submit():
            user = Users(email_address=loginform.email_address.data, 
                password=generate_password_hash(loginform.password.data, method='sha256'),
            )
            
            email_address = Users.query.filter_by(email_address=loginform.email_address.data).first()
            password = Users.query.filter_by(password=loginform.password.data).first()

            # check if the user actually exists
            # take the user-supplied password, hash it, and compare it to the hashed password in the database
            if not email_address or password != user.password:
                flash('Please check your username and password and try again')
                errors = True

            if errors:
                return redirect(url_for('login')) # if the user doesn't exist or password is wrong, reload the page
        return redirect(url_for('profile'))
    return render_template('login.html', form=loginform)

# create route to logout
@app.route('/logout')
def logout():
    return 'logout.html'

# create route to view profile
@app.route('/profile')
def profile():
    return 'profile.html'