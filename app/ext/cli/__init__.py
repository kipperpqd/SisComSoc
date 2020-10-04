import click #ferramenta que ja vem com o flask
from app.ext.db import db
from app.ext.auth.models import User


def init_app(app):

    @app.cli.command()
    def create_db():
        db.create_all()
        click.echo("DataBse criado com sucesso")    
    