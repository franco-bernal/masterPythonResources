import os
import socket

# Crear un socket TCP
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establecer la dirección y puerto del servidor
server_address = ('127.0.0.1', 9000)

# Conectar con el servidor
client_socket.connect(server_address)

print("Conectado con el servidor en", server_address)

# Enviar el archivo al servidor
file_name = "x.txt"
file_size = os.path.getsize(file_name)

# Enviar el tamaño del archivo como un número entero
client_socket.sendall(str(file_size).encode())

# Enviar el contenido del archivo
with open(file_name, 'rb') as file:
    file_data = file.read()
    client_socket.sendall(file_data)

print("Archivo enviado al servidor")

# Cerrar la conexión con el servidor
client_socket.close()