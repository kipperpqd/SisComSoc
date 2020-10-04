from flask_admin.contrib.sqla import ModelView
from flask import Markup
from app.ext.auth.models import User
from app.ext.db import db




class UserAdmin(ModelView):
    column_searchable_list = ["email", "passwd"] 