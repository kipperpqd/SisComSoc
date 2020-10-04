from flask import render_template
from flask import Blueprint
from flask import current_app

bp = Blueprint("site",__name__)

@bp.route('/')
def index():
    current_app.logger.debug("Entrei na função main, (modo debug)")
    return render_template("index.html")