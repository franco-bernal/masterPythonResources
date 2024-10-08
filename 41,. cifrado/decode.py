import base64

def cifrar_archivo(archivo, veces):
    with open(archivo, 'r') as f:
        contenido = f.read()

    for _ in range(veces):
        contenido = base64.b64encode(contenido.encode()).decode()

    return contenido

def decodificar_contenido(contenido, veces):
    for _ in range(veces):
        contenido = base64.b64decode(contenido.encode()).decode()

    return contenido

archivo = 'x.txt'
veces = 100

contenido_cifrado = cifrar_archivo(archivo, veces)

print("Contenido cifrado:")
print(contenido_cifrado)

contenido_decodificado = decodificar_contenido(contenido_cifrado, veces)

print("\nContenido decodificado:")
print(contenido_decodificado)