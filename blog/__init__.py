from flask  import Blueprint

blog = Blueprint('blog_bp', __name__, template_folder='templates', static_folder='static')