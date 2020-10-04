from flask_debugtoolbar import DebugToolbarExtension
from flask import current_app


def init_app(app):
    #current_app.logger.debug("init_app (DebugToolBar)")
    DebugToolbarExtension(app)