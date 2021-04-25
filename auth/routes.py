from auth import bp
from database import db

from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from werkzeug.security import generate_password_hash

from .forms import RegistrationForm, LoginForm
from .models import User


@bp.route('/register', methods=('GET', 'POST'))
def register():
    """
    When the user visits the /auth/register URL, the register view will return HTML with a form for them to fill out.
    When they submit the form, it will validate their input and either show the form again with an error message or
    create the new user and go to the login page.
    :return: Upon successful registration the user is redirected to login page. Otherwise page is reloaded with messages
    """

    # If user is already logged in, redirect them to index page
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # Create the Form
    print("Start of Registration Route")
    form = RegistrationForm()

    # Validate Form for POST submissions and create new user in database
    if form.validate_on_submit():
        # Create User object
        user = User(form.first_name.data,
                    form.last_name.data,
                    form.username.data,
                    form.email.data,
                    form.phone_number.data)
        user.set_password(form.password.data)

        # Add New User to database
        db.session.add(user)
        db.session.commit()
        print("New User added to database.")

        # Flash success message and redirect to login page
        flash("Registration Successful!!")
        return redirect(url_for('auth.login'))

    # For GET requests render the register template
    return render_template('auth/register.html', form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    A function that accomplishes login functionality:
        - Checks for a registered username, if correct
        - Checks for a valid password, if both correct
        - Adds user.id to the session
    :return: Once successful login occurs, the user is redirected to index page.
    """

    # Check to see if user is already logged in.
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    # Create the Form
    form = LoginForm()

    # Validate form for POST submissions and verify user
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        print(user)
        if user is None:
            flash('Invalid username')
            return redirect(url_for('auth.login'))
        if not user.check_password(form.password.data):
            print("User's hash: ", user.password_hash)
            print("Form's hash: ", generate_password_hash(form.password.data))
            flash('Invalid password')
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))

    # GET Requests render the login template
    return render_template('auth/login.html', form=form)


@bp.route('/logout')
def logout():
    """
    A route to logout the user. It clears the session object and then
    directs them to the index page of the site.
    :return: redirect function to the 'index' url
    """
    logout_user()
    flash("You have successfully been logged out.")
    return redirect(url_for('login'))
