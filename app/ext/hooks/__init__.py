def init_app(app):
    
    @app.before_first_request
    def init_evreything():
        print("Estou iniciando o app")