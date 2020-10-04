from app.ext.auth import models
from app.ext.auth.commands import list_users, add_user


from app.ext.db import db

from app.ext.auth.admin import UserAdmin

from app.ext.auth.models import User
from app.ext.admin import admin


def init_app(app):
    app.cli.command()(list_users) #forma de chamar a funçao sem decoradores
    app.cli.command()(add_user)
    """flask simple login + JWT"""
    
    admin.add_view(UserAdmin(User, db.session))
        