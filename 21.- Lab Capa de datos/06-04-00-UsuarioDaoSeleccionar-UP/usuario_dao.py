from cursor_del_pool import CursorDelPool
from logger_base import log
from usuario import Usuario

class UsuarioDAO:
    '''
    DAO - Data Access Object para la tabla de usuario
    CRUD - Create - Read - Update - Delete para la tabla de usuario
    '''
    _SELECT = 'SELECT * FROM usuario ORDER BY id_usuario'
    _INSERTAR = 'INSERT INTO usuario(username, password) VALUES(%s, %s)'
    _ACTUALIZAR = 'UPDATE usuario SET username=%s, password=%s WHERE id_usuario=%s'
    _ELIMINAR = 'DELETE FROM usuario WHERE id_usuario=%s'
'''
Este fragmento de código en Python define un método de clase 
llamado "seleccionar" que pertenece a una clase (se refiere a "cls").

El método utiliza un gestor de contexto "CursorDelPool" 
para administrar un cursor de base de datos. Registra un 
mensaje de depuración, ejecuta una consulta SQL utilizando el cursor,
 recupera todos los resultados y luego crea instancias de la 
 clase "Usuario" para cada registro. Finalmente, devuelve 
 una lista de estas instancias de "Usuario".

La consulta SQL se define por la variable de clase 
"_SELECT", que presumiblemente es una cadena de texto 
que contiene una declaración SQL SELECT.
'''
    @classmethod
    def seleccionar(cls):
        with CursorDelPool() as cursor:
            log.debug('Seleccionando usuarios')
            cursor.execute(cls._SELECT)
            registros = cursor.fetchall()
            usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0], registro[1], registro[2])
                usuarios.append(usuario)
            return usuarios

