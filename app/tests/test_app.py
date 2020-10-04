def test_app_is_created(app):
    assert app.name == 'siscomsoc.app'
    
def test_app_is_loaded(config):
    assert config["DEBUG"] is False

def test_request_return_404(client):
    assert client.get("/url_que_não_existe").status_code == 404
    
def test_app_is_created(app):
    assert app.name == 'siscomsoc.app'