import requests

api_url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_VzH3SzmlAwDS0bEYi6VMoq39ZhsDAmAxU2AWfo7K&currencies="

#Structural Facade Design Pattern
#Se oculta la lógica de comunicación con la API de cambio de moneda, de la API de la lógica de negocio.
#La aplicación solo sabe que debe enviar un código de moneda a la función y esta se encargará de manejar el HTTP request y parseo de la respuesta para solo retornar el número a ocupar en la lógica.
class Facade:

    def currency_operation(currency_key):
        op1 = consult_exchange_api(currency_key)

        return op1


def consult_exchange_api(currency_key):
    data = requests.get(f'{api_url}{currency_key}').json()
    return data["data"][currency_key]

