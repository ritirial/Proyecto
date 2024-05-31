import requests

api_url = "https://api.freecurrencyapi.com/v1/latest?apikey=fca_live_VzH3SzmlAwDS0bEYi6VMoq39ZhsDAmAxU2AWfo7K&currencies="

def get_currency(currency_key):
    data = requests.get(f'{api_url}{currency_key}').json()
    return data["data"][currency_key]