# Definir una metaclase
class MiMetaclase(type):
    def __init__(cls, nombre, bases, dct):
        print(f"Creando la clase {nombre}")
        super().__init__(nombre, bases, dct)

# Usar la metaclase para definir una nueva clase
class MiClase(metaclass=MiMetaclase):
    pass

# Crear una instancia de la clase
objeto = MiClase()
