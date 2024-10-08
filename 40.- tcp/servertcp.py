import socket
import threading

class ServidorTCP:
    def __init__(self, host, puerto):
        self.host = host
        self.puerto = puerto
        self.servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.servidor.bind((self.host, self.puerto))
        self.servidor.listen(5)
        print(f"Servidor escuchando en {self.host}:{self.puerto}")

    def manejar_cliente(self, cliente, direccion):
        print(f"Conexión establecida con {direccion}")
        while True:
            mensaje = cliente.recv(1024).decode()
            if mensaje:
                print(f"Mensaje recibido de {direccion}: {mensaje}")
                respuesta = input("Ingrese respuesta: ")
                cliente.send(respuesta.encode())
            else:
                print(f"Conexión cerrada con {direccion}")
                cliente.close()
                break

    def iniciar(self):
        while True:
            cliente, direccion = self.servidor.accept()
            thread = threading.Thread(target=self.manejar_cliente, args=(cliente, direccion))
            thread.start()

if __name__ == "__main__":
    servidor = ServidorTCP("localhost", 3000)
    servidor.iniciar()