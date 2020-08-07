from flask  import Blueprint

bp = Blueprint('blog', __name__, template_folder='templates', static_folder='static', url_prefix='/blog')
