import pytest
from datetime import datetime
import grocery.repository.grocery_repository as grocery_repository


#Objeto de prueba para test
@pytest.fixture
def test_item():
    return grocery_repository.Item(
        SKU = 'W357',
        Name = 'Pytest Item',
        Description = 'An item to add from pytest',
        Quantity = 300,
        Price = 12.99,
        Expiration_date = datetime.strptime('2025-05-28', '%Y-%m-%d')
    )


#Test confirma que la BD aumentó al agregar item
def test_item_add(test_item):
    assert test_item is not None

    repository = grocery_repository.SqlAlchemyRepository()
    repository.clean_database()
    
    tamano = len(repository.get())

    repository.add(test_item)

    assert len(repository.get()) > tamano

    repository.clean_database()
