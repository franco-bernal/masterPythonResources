# Crear una clase usando 'type'
MiClase = type('MiClase', (object,), {'valor': 10, 'mostrar': lambda self: print(self.valor)})

# Crear una instancia de la clase
objeto = MiClase()
objeto.mostrar()  # Salida: 10
