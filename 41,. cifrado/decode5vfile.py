import base64

def decodificar_archivo(archivo, veces):
    with open(archivo, 'r') as f:
        contenido = f.read()

    for _ in range(veces):
        contenido = base64.b64decode(contenido.encode()).decode()

    return contenido

archivo_cifrado = 'x2.txt'
archivo_plano = 'x3.txt'
veces = 50

contenido_plano = decodificar_archivo(archivo_cifrado, veces)

with open(archivo_plano, 'w') as f:
    f.write(contenido_plano)

print(f"Contenido plano escrito en {archivo_plano}")