"""
This file will hold all the configuration mappings for this app.
Ensure no secrets are kept in this file as it will be uploaded to GitHub.
Secrets should be set as OS Environment Variables or kept in an instance file.
"""
import os
from os import urandom

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    # Secret Key
    SECRET_KEY = urandom(16)

    # SqlAlchemy Config
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
