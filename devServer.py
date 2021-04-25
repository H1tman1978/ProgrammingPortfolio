import os

from flask import Flask
from flask import render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config

# Create necessary extension Global Objects
login_manager = LoginManager()
migrate = Migrate()


@login_manager.user_loader
def load_user(user_id):
    from auth.models import User
    print("Load User Function Generated...")
    return User.query.get(int(user_id))


def create_app(test_config=None):
    # create and configure the app
    print("Setting up Flask App")
    app = Flask(__name__, instance_relative_config=True)

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_object(Config)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Load flask extensions here

    # Flask-Login
    print("Configuring Login Manager")
    login_manager.init_app(app)

    # Load blueprints here
    print("Loading Blueprints...")
    from blog import bp as blog_bp
    app.register_blueprint(blog_bp)

    from auth import bp as auth_bp
    app.register_blueprint(auth_bp)

    # Configure Database connection
    print("Configuring Database Connection")
    from database import db
    db.init_app(app)
    db.create_all(app=app)
    migrate.init_app(app, db)

    # Route to main Portfolio page
    @app.route('/')
    def index():
        return render_template('index.html')

    return app


if __name__ == '__main__':
    flask_app = create_app()
    flask_app.run()
