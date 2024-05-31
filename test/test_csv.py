import pytest
from grocery.handler.csv_handler import read_csv_to_dict


#Genera un diccionario con el archivo
@pytest.fixture
def test_items():
    return read_csv_to_dict('sample_grocery.csv')


#Test confirma que el csv genera una lista no vacía
def test_read_file(test_items):
    #comprueba que read_csv_to_dict si generó una lista
    assert test_items is not None

    #comprueba que hay datos en el diccionario
    assert len(test_items) > 0