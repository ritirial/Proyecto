import pytest
from grocery.main import app

#Cliente de prueba para testing de rutas
@pytest.fixture
def client():
    app.config.update( {'TESTING': True} )
    with app.test_client() as client:
        yield client
    

#Test confirma que la API de conversión regresa un valor numérico
def test_retrieve_items_route(client):
    resp = client.get('/item')
    assert b'Grocery List Application' in resp.data