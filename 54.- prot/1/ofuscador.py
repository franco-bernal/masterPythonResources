import ast
import astor
import random
import string

# Función para generar nombres aleatorios
def generar_nombre_longitud(largo):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=largo))

# Clase para visitar y transformar nodos en el árbol AST
class Ofuscador(ast.NodeTransformer):
    def __init__(self):
        self.nombre_mapping = {}
        self.contador = 0

    def transformar_nombre(self, nombre):
        if nombre not in self.nombre_mapping:
            nuevo_nombre = generar_nombre_longitud(8)
            self.nombre_mapping[nombre] = nuevo_nombre
        return self.nombre_mapping[nombre]

    def visit_FunctionDef(self, node):
        node.name = self.transformar_nombre(node.name)
        self.generic_visit(node)
        return node

    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Store):
            node.id = self.transformar_nombre(node.id)
        elif isinstance(node.ctx, ast.Load):
            node.id = self.transformar_nombre(node.id)
        return node

def ofuscar_codigo(archivo_fuente, archivo_ofuscado):
    with open(archivo_fuente, 'r') as f:
        codigo = f.read()

    arbol = ast.parse(codigo)
    ofuscador = Ofuscador()
    arbol_ofuscado = ofuscador.visit(arbol)
    codigo_ofuscado = astor.to_source(arbol_ofuscado)

    with open(archivo_ofuscado, 'w') as f:
        f.write(codigo_ofuscado)

    print(f"Archivo ofuscado guardado en: {archivo_ofuscado}")

# Ejecutar el script de ofuscación
archivo_fuente = 'mi_codigo.py'
archivo_ofuscado = 'mi_codigo_ofuscado.py'
ofuscar_codigo(archivo_fuente, archivo_ofuscado)
