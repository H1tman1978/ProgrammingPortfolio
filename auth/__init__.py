from flask import Blueprint


bp = Blueprint('auth', __name__, url_prefix='/auth', template_folder='templates', static_folder='static')


import auth.routes
import auth.models
import auth.forms
