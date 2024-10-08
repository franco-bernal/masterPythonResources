from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend

def generar_llaves():
    # Generar una nueva clave RSA
    clave_privada = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    # Obtener la clave pública
    clave_publica = clave_privada.public_key()
    # Serializar las claves
    clave_privada_serializada = clave_privada.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    clave_publica_serializada = clave_publica.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    return clave_privada_serializada, clave_publica_serializada

def codificar_mensaje(mensaje, clave_publica_serializada):
    # Cargar la clave pública
    clave_publica = serialization.load_pem_public_key(
        clave_publica_serializada,
        backend=default_backend()
    )
    # Codificar el mensaje
    mensaje_codificado = clave_publica.encrypt(
        mensaje,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return mensaje_codificado

def descodificar_mensaje(mensaje_codificado, clave_privada_serializada):
    # Cargar la clave privada
    clave_privada = serialization.load_pem_private_key(
        clave_privada_serializada,
        password=None,
        backend=default_backend()
    )
    # Descodificar el mensaje
    mensaje_descodificado = clave_privada.decrypt(
        mensaje_codificado,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return mensaje_descodificado

def main():
    # Generar las llaves
    clave_privada_serializada, clave_publica_serializada = generar_llaves()
    # Leer el archivo x.txt
    with open('x.txt', 'rb') as archivo:
        mensaje = archivo.read()
    # Codificar el mensaje
    mensaje_codificado = codificar_mensaje(mensaje, clave_publica_serializada)
    # Crear un nuevo archivo con el mensaje codificado
    with open('mensaje_codificado.txt', 'wb') as archivo:
        archivo.write(mensaje_codificado)
    # Descodificar el mensaje
    mensaje_descodificado = descodificar_mensaje(mensaje_codificado, clave_privada_serializada)
    # Imprimir el mensaje descodificado
    print(mensaje_descodificado.decode('utf-8'))
    # Crear un nuevo archivo con el mensaje descodificado
    with open('mensaje_descodificado.txt', 'wb') as archivo:
        archivo.write(mensaje_descodificado)

if __name__ == '__main__':
    main()