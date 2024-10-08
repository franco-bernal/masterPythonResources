import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona(nombre, apellido, email) VALUES(%s, %s, %s)'
            valores = (
                ('x', 'Cantu', 'mcantu@mail.com'),
                ('y', 'Quintana', 'aquintana@mail.com'),
                ('z', 'Gonzalez', 'mgonzalez@mail.com')
            )
            cursor.executemany(sentencia, valores)
            # conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros Insertados: {registros_insertados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()