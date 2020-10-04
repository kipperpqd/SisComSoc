from app.ext import configuration


from flask import Flask


def create_app():  # create app é  uma convenção do flask
    app = Flask(__name__)  # __name__ é o nome do pacote (SISCOMSOC)
    configuration.init_app(app)
       
    return app