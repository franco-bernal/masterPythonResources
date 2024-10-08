import requests

def enviar_mensaje(nombre):
    url = "http://localhost:5000/saludo"
    params = {"nombre": nombre}
    response = requests.get(url, params=params)
    print(response.text)

enviar_mensaje("vegeta666 ")
enviar_mensaje("saybanmane")