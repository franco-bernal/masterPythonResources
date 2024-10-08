import base64

def cifrar_archivo(archivo, veces):
    with open(archivo, 'r') as f:
        contenido = f.read()

    for _ in range(veces):
        contenido = base64.b64encode(contenido.encode()).decode()

    return contenido

archivo = 'x.txt'
veces = 5

contenido_cifrado = cifrar_archivo(archivo, veces)

print(contenido_cifrado)