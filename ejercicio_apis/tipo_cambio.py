import requests

respuesta=requests.get("https://open.er-api.com/v6/latest/USD")
print("Codigo de estado:",respuesta.status_code)