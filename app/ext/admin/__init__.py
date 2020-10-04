from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from app.ext.db import db

from app.ext.db.models import Cad_cmt_om

admin = Admin()

def init_app(app):
    admin.name = app.config.get("ADMIN_NAME", "SisComSoc")
    admin.template_mode = app.config.get("ADMIN_TEMPLATE_MODE", "bootstrap3")
    admin.init_app(app)    
    
    admin.add_view(ModelView(Cad_cmt_om, db.session))