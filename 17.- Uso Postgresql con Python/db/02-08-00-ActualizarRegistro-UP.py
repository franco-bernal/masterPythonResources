import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_db')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'UPDATE persona SET nombre=%s, apellido=%s, email=%s WHERE id_persona=%s'
            valores = ('Juan Carlosxx', 'Juarez', 'jcjuarez@mail.com', 1)
            cursor.execute(sentencia, valores)
            registros_actualizados = cursor.rowcount
            print(f'Registros Actualizados: {registros_actualizados}')
except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()