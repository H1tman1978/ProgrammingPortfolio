import functools

from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

from blog.db import get_db


bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates', static_folder='static')


@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    When the user visits the /auth/register URL, the register view will return HTML with a form for them to fill out.
    When they submit the form, it will validate their input and either show the form again with an error message or
    create the new user and go to the login page.
    :return: Upon successful registration the user is redirected to login page. Otherwise page is reloaded with messages
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required'
        elif not password:
            error = 'Password is required'
        elif db.execute(
            'SELECT id FROM user WHERE username = ?', (username,)
        ).fetchone() is not None:
            error = f"User {username} is already registered."

        if error is None:
            db.execute(
                'INSERT INTO user (username, password_hash) VALUES (?, ?)',
                (username, generate_password_hash(password))
            )
            db.commit()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    A function that accomplishes login functionality:
        - Checks for a registered username, if correct
        - Checks for a valid password, if both correct
        - Adds user.id to the session
    :return: Once successful login occurs, the user is redirected to index page.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        elif not check_password_hash(user['password_hash'], password):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('blog.index'))

        flash(error)

    return render_template('auth/login.html')


@bp.before_request
def load_logged_in_user():
    """
    At the beginning of each request, if a user is logged in, their information
    will be loaded and made available to other views.
    :return: N/A
    """
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id)
        ).fetchone()


def login_required(view):
    """
    This decorator returns a new view function that wraps the original view it’s applied to.
    The new function checks if a user is loaded and redirects to the login page otherwise.
    If a user is loaded the original view is called and continues normally. You’ll use this
    decorator when writing the blog views.
    :param view: the function that is to be wrapped by the decorator. In other words,
                 the view or route you require that the user to be logged in.
    :return: If the user is logged in, the wrapped view is returned, otherwise user is
             redirected to login page
    """
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
