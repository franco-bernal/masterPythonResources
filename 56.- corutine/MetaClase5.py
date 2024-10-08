class ConfiguracionMeta(type):
    def __init__(cls, nombre, bases, dct):
        # Verificar que el atributo 'nombre' esté definido
        if 'nombre' not in dct:
            raise TypeError(f"La clase {nombre} debe definir el atributo 'nombre'")

        # Verificar que el método 'cargar' esté definido
        if 'cargar' not in dct or not callable(dct['cargar']):
            raise TypeError(f"La clase {nombre} debe definir un método llamado 'cargar'")

        # Verificar que el método 'guardar' esté definido
        if 'guardar' not in dct or not callable(dct['guardar']):
            raise TypeError(f"La clase {nombre} debe definir un método llamado 'guardar'")

        super().__init__(nombre, bases, dct)
