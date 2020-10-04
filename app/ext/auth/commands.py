import click
from app.ext.db import db
from app.ext.auth.models import User

def list_users():
    users = User.query.all()
    click.echo(f"Lista de Usuarios: {users}")
 
@click.option("--email", "-e")    
@click.option("--passwd", "-p")
@click.option("--admin", "-a", is_flag=True, default=False)
def add_user(email, passwd, admin):
    user = User(
        email=email,
        passwd=passwd,
        admin=admin
    )
    db.session.add(user)
    db.session.commit()
    click.echo(f"Usuário {email} criado com sucesso")