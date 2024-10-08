import socket

def main():
    # Configuración del servidor
    host = 'localhost'
    puerto = 12345

    # Crear un objeto socket
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Conectar al servidor
    cliente.connect((host, puerto))

    print("Conectado al servidor")

    # Bucle para mantener la conexión abierta
    while True:
        # Leer mensaje desde la terminal
        mensaje = input("Ingrese un mensaje: ")

        # Enviar mensaje al servidor
        cliente.send(mensaje.encode())

        # Recibir respuesta del servidor
        respuesta = cliente.recv(1024).decode()
        print("Respuesta del servidor:", respuesta)

if __name__ == "__main__":
    main()