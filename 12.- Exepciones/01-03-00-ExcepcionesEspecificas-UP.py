resultado = None
a = '10'
b = 0
try:
    resultado = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError: {e} , {type(e)}')
except TypeError as e:
    print(f'Solo numeros : {e} , {type(e)}')
except Exception as e:
    print(f'Exception : {e} , {type(e)}')

print(f'Resultado: {resultado}')
print('Continuamos...')