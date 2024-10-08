import base64

def cifrar_archivo(archivo, veces):
    with open(archivo, 'r') as f:
        contenido = f.read()

    for _ in range(veces):
        contenido = base64.b64encode(contenido.encode()).decode()

    return contenido

archivo_original = 'x.txt'
archivo_cifrado = 'x2.txt'
veces = 50

contenido_cifrado = cifrar_archivo(archivo_original, veces)

with open(archivo_cifrado, 'w') as f:
    f.write(contenido_cifrado)

print(f"Contenido cifrado escrito en {archivo_cifrado}")