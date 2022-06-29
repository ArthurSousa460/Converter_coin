import requests


def get_value_coin():
    request = requests.get('https://economia.awesomeapi.com.br/last/BTC-BRL')
    data = request.json()
    coin = float(data['BTCBRL']['bid'])
    return coin
    


def converter_of_coin(bitcoin):
    real = get_value_coin()
    value_converting =  real * bitcoin
    return value_converting