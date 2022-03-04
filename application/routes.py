from application import app, db
from application.models import Users, Exercises, Workout_Plans
from application.forms import CreateAccountForm
from flask import render_template, redirect, url_for, request

# create for homepage
@app.route('/home')
@app.route('/', methods=['GET', 'POST'])

# create route for account creation
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    message = ""
    createform = CreateAccountForm()

    if request.method == 'POST':
        
        if createform.validate_on_submit():
            user = Users(user_name=createform.user_name.data, 
                password=createform.password.data, 
                first_name=createform.first_name.data, 
                last_name=createform.last_name.data, 
                email_address=createform.email_address.data
            )
            db.session.add(user)
            db.session.commit()       
        # Instead of rendering a template, the next line redirects the user to the endpoint for the function called 'read'.
        # return redirect(url_for('signup', message="Your account has been created"))
    return render_template('signup.html', form=createform)