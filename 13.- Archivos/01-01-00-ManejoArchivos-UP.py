try:
    archivo = open('prueba3.txt', 'w')
    archivo.write('Agregamos información al archivo\n')
    archivo.write('Adios')
except Exception as e:
    print(e)
finally:
   archivo.close()