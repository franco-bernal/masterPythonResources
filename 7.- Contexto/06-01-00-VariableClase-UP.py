#python -m http.server 8000 -d path
class MiClase:

    variable_clase = '234234234'

    def __init__(self, variable_instancia):
        self.variable_instancia = variable_instancia

print(MiClase.variable_clase)

x = MiClase('Valor interno a instancia')

print(x.variable_instancia)
print(x.variable_clase)

x2 = MiClase('xxx')

print(x2.variable_instancia)
print(x2.variable_clase)

