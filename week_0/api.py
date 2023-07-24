import requests

URL = "https://www.alphavantage.co/query"

parameters = {
    'function': "FX_DAILY",
    "from_symbol": "NZD",
    "to_symbol": "VND",
    "apikey": "8YKT20RWYR84QME9"
}

response = requests.get(URL, params=parameters)
data = response.json()
print(data)
