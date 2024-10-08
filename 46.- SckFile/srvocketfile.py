import socket
import datetime

# Crear un socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Establecer la dirección y puerto del servidor
server_address = ('127.0.0.1', 9000)

# Enlazar el socket con la dirección y puerto
server_socket.bind(server_address)

# Escuchar conexiones entrantes
server_socket.listen(1)

print("Servidor TCP escuchando en", server_address)

while True:
    # Esperar a que un cliente se conecte
    client_socket, client_address = server_socket.accept()

    print("Conexión establecida con", client_address)

    # Recibir el tamaño del archivo como un número entero
    file_size_str = client_socket.recv(1024).decode()

    if file_size_str == '':
        print("No se recibió el tamaño del archivo")
        break

    file_size = int(file_size_str)

    print("Tamaño del archivo:", file_size)

    # Recibir el contenido del archivo
    file_data = b''
    while len(file_data) < file_size:
        chunk = client_socket.recv(1024)
        file_data += chunk

    print("Archivo recibido:", file_data)

    # Crear un nuevo archivo con el nombre de la fecha y hora en que llegó el archivo
    fecha_hora = datetime.datetime.now()
    new_file_name = fecha_hora.strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    print("Nombre del archivo:", new_file_name)

    try:
        with open(new_file_name, 'wb') as new_file:
            new_file.write(file_data)
    except Exception as e:
        print("Error al escribir el archivo:", e)

    # Cerrar la conexión con el cliente
    client_socket.close()