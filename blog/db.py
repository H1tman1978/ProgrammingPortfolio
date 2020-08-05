import sqlite3
import click

from flask import current_app, g
from flask.cli import with_appcontext


def get_db():
    """
    A function that returns the database connection in the request element "g"
    If there's no db element in "g" it connects to the db in the "DATABASE"
    field of the application configuration and creates that portion of the "g"
    element of the request field.

    :return: g.db
    """
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    """
    checks if a connection was created by checking if g.db was set.
    If the connection exists, it is closed.
    :param e: Any error message to pass
    :return: Nothing. The database connection is simply closed.
    """
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    """
    This function initializes the database for the blog blueprint.
    :return: an initialized database
    """
    db = get_db()

    with current_app.open_resource('blog\schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    Clear the existing data and create new tables
    :return: No value is returned
    """
    init_db()
    click.echo('Initialized the database.')



def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
