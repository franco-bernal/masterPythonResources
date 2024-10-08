from cryptography.fernet import Fernet

try:
    # Genera una clave
    clave = Fernet.generate_key()
    cipher_suite = Fernet(clave)

    # Cifra el contenido
    with open('mi_codigo.py', 'rb') as f:
        contenido = f.read()

    contenido_cifrado = cipher_suite.encrypt(contenido)

    # Guarda el contenido cifrado
    with open('mi_codigo_cifrado.pyc', 'wb') as f:
        f.write(contenido_cifrado)
    print("Archivo cifrado creado correctamente.")

    # Para descifrarlo en tiempo de ejecución
    with open('mi_codigo_cifrado.pyc', 'rb') as f:
        contenido_cifrado = f.read()

    contenido_descifrado = cipher_suite.decrypt(contenido_cifrado)

    with open('mi_codigo_descifrado.py', 'wb') as f:
        f.write(contenido_descifrado)
    print("Archivo descifrado creado correctamente.")

except Exception as e:
    print(f"Ocurrió un error: {e}")
