import requests

respuesta=requests.get("https://open.er-api.com/v6/latest/USD")
print("Codigo de estado:",respuesta.status_code)

datos = respuesta.json()
print("Moneda base",datos["base_code"])
print("1 USD =",datos ["rates"]["GTQ"],"GTQ")
print("1 USD= ",datos ["rates"]["EUR"],"EUR")