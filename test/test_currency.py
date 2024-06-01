from grocery.grocery_utils import currency_client


#Test confirma que la API de conversión regresa un valor numérico
def test_retrieve_conversion():
    currency_calculation = currency_client.Facade.currency_operation('MXN')
    assert currency_calculation > 0 