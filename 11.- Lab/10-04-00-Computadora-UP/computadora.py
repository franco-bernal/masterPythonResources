from monitor import Monitor
from raton import Raton
from teclado import Teclado

class Computadora:
    contador_computadoras = 0

    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._raton = raton

    def __str__(self):
        return f'''
        {self._nombre}: {self._id_computadora}
        Monitor: {self._monitor}
        Teclado: {self._teclado}
        Ratón: {self._raton}
        '''
if __name__ == '__main__':
    teclado1 = Teclado('HP', 'USB')
    raton1 = Raton('HP', 'USB')
    monitor1 = Monitor('HP', 15)
    computadora1 = Computadora('HPx', monitor1, teclado1, raton1)
    print(computadora1)
    
    teclado2 = Teclado('Acer', 'Bluetooth')
    raton2 = Raton('Acer', 'Bluetooth')
    monitor2 = Monitor('Acer', 27)
    
    computadora2 = Computadora('Acer', monitor2, teclado2, raton2)
    
    print(computadora2)
     
    teclado3 = Teclado('Acer', 'Bluetooth')
    raton3 = Raton('Acer', 'Bluetooth')
    monitor3 = Monitor('Acer', 27)
    
    computadora3 = Computadora('x', monitor3, teclado3, raton1)
    print(computadora3)