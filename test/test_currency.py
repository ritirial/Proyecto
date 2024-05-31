from grocery.repository.currency_client import get_currency


#Test confirma que la API de conversión regresa un valor numérico
def test_retrieve_conversion():

    assert get_currency('MXN') > 0 