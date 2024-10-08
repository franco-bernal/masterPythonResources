'''

Bien, como podemos observar en la figura, recordamos los ejercicios de figura geométrica.
Recordemos que esta clase no contiene el método de área debido a que la clase figura geométrica no sabe
calcular el área.
Si no hemos especificado cuál es el tipo de figura geométrica que vamos a calcular.
Por ejemplo.
Un cuadrado rectángulo.
Etcétera.
Así que en este caso hasta el código que hemos creado no hemos agregado el método de área.
Sin embargo, para obligar a las clases hijas a definir el método de área, podemos agregar un método
abstracto.
Así que, en este caso, un método abstracto no va a tener implementación.
Pero lo que vamos a conseguir es que si agregamos este método a la clase padre, vamos a obligar a las
clases hijas a agregar una implementación tal cual como ya lo hemos trabajado en las clases hijas.
De momento era opcional agregar el método de calcular área.
Así que en este caso, los métodos definidos de calcular área en las clases hijas ahora ya va a ser
obligatorio.
No solamente va a ser opcional como anteriormente, sino que si definimos un método abstracto en la
clase padre, obligamos a las clases hijas a agregar esta implementación.
Ahora, si en una clase agregamos un método abstracto, toda la clase se vuelve también abstracta.
Esto quiere decir que no podemos crear instancias u objetos de una clase abstracta.
Así que en la clase figura geométrica no podemos crear objetos.
Y esto en nuestro modelo está bien, ya que la clase de figura geométrica no tiene sentido que no distanciemos
si no sabemos realmente cuál es el tipo de figura que vamos a trabajar.
Así que solamente es conveniente que podamos crear objetos de las clases hijas, como puede ser cuadrado,
rectángulo, triángulo, etcétera.
Así que vamos a realizar estas modificaciones para convertir nuestra clase de figura geométrica en una
clase abstracta.
Definir nuestro método de calcular área como un método abstracto y finalmente obligar a las clases hijas
a implementar este método.
La implementación en las clases hijas ya lo tenemos, así que no vamos a ver ninguna diferencia de código
en las clases hijas, pero si vamos a estar obligados a realizar esta implementación y en cambio en
la clase padre, si vamos a convertir esta clase padre en una clase abstracta, bien, vamos a revisar
estos cambios en nuestro código.
En la clase de figura geométrica vamos a realizar lo siguiente Para convertir esta clase en una clase
abstracta, tenemos que extender de otra clase.
A su vez, en este caso, la clase abecé.
Qué significa?
Abstract Voice Class Así que es la clase base en Python para convertir una clase en clase abstracta.
Vamos a importar esta clase del módulo de abecé, el módulo de Abstract Voice class.
Ese es el módulo e importamos la clase de abecé, ya que vamos a extender de esta clase y también vamos
a importar un decorador.
El decorador de Abstract Method, este decorador lo vamos a utilizar para definir un método abstracto.
Bien, una vez que ya realizamos estas importaciones, la clase de figura geométrica para convertirla
en una clase abstracta va a extender de la clase abecé.
Abstract Las clases.
Y dentro de esta clase de figura geométrica vamos a agregar el método calcular área.
Primero tenemos el método init.
Posteriormente los métodos jet set.
Y después de estos métodos vamos a agregar nuestro método abstracto.
Este método va a tener el decorador de Abstract Method para que pueda considerarse este método un método
abstracto.
Posteriormente definimos nuestro método calcular área.
Sin embargo, este método no contiene ninguna implementación, ya que recordemos que no podemos calcular
el área de una figura geométrica que desconocemos.
Por lo tanto, simplemente indicamos que pase este método.
Es decir, que no tiene ninguna implementación.
Recordemos que únicamente lo utilizamos para definir correctamente nuestro método, pero estamos indicando
que no tiene ninguna implementación y además estamos indicando que es un método abstracto.
Así que además, no puede contener ninguna implementación.
Bien, con estos cambios vamos a realizar una prueba.
Si tratamos de crear un objeto de la clase de figura abstracta, definimos una variable llamada figura.
Y tratamos de crear un objeto de esta clase.
Vamos a importarla.
Ya le hemos importado, ejecutamos.
Podemos observar que nos manda el mensaje type error fue un error de tipo no podemos instanciar una
clase abstracta, en este caso la clase abstracta llamada figura geométrica, y nos está indicando que
contenemos un método abstracto llamado calcular área.
Así que vamos a poner el comentario.
No se puede instanciar una clase abstracta.
Y ponemos este link entre comentarios para que podamos continuar con nuestro programa.
Y con esto ya estamos comprobando que entonces no podemos inicializar un objeto de la clase de figura
geométrica, ya que es una clase abstracta.
Y ahora si ejecutamos nuestro código.
Podemos observar que funciona sin ningún problema, ya que estamos realizando el cálculo del área y
el cálculo del rectángulo con los valores que hemos descrito.
Recordemos que hemos agregado algunas validaciones, como ya vimos anteriormente.
Así que debido a que las clases hijas ya han agregado una implementación del método Calcular Área,
no tenemos ningún problema para ejecutar nuestra prueba.
Sin embargo, si una de las clases hijas no agrega esta implementación, por ejemplo, si vamos a la
clase de cuadrado y quitamos la implementación del método Calcular Área, vamos a ponerlo entre comentarios
y ejecutamos nuestra prueba.
Podemos ver que nos dice que también no podemos instanciar la clase abstracta cuadrado, ya que no hemos
definido el método calcular área y debido a que el método calcular área C heredó de la clase padre.
Entonces ese método es abstracto, se hereda a la clase hija, la clase cuadrado y por lo tanto también
la clase cuadrado se convierte en una clase abstracta con un método abstracto que tengamos definido
en una clase, toda la clase se convierte en una clase abstracta.
Por lo tanto, tampoco podemos crear objetos de la clase cuadrado.
Y entonces, para ello es que nos sirve definir métodos abstractos para obligar a las clases hijas a
que agreguen la implementación de los métodos abstractos y debido a que en este momento ya estamos agregando
la implementación, el método calcular área, ya estamos agregando este código para realizar la implementación.
Entonces no tenemos ya ningún problema para ejecutar nuestro código.
Y lo mismo sucede con la clase de rectángulo.
Bien, por último, un comentario extra recordemos que hicimos algunas validaciones en los métodos Zeth
de las clases de cuadrado y rectángulos.
Si no quisiéramos que estos valores se pudieran modificar una vez que se inicializado nuestro objeto,
entonces recordemos que podemos hacer estas propiedades como de sólo lectura y para ello simplemente
tendríamos que ir a nuestra clase de figura geométrica.
Y quitar los métodos set, por ejemplo, en este caso el método set para modificar el valor de ancho
y el método Set para modificar el valor de alto.
Esto ya no tiene que ver con las clases abstractas, sino que simplemente es un cambio, una mejora
que podríamos hacer en dado caso de que no quisiéramos que una vez que hemos asignado un valor en la
inicialización de los objetos, si ya no queremos que se modifique, entonces podemos convertir los
atributos de solo lectura y que ya no se pueda ejecutar este código.
Vamos a comprobar.
Podemos saber que ya no podemos modificar el atributo debido a que es un atributo de solo lectura.
Así que este código ya lo tendríamos que poner entre comentarios.
Bien, de momento ya lo dejamos a su decisión si permiten esta modificación debido a los métodos СЕНТЯБРЯ
o si evitan esta modificación y únicamente permiten la inicialización de los valores al momento de crear
su objeto.
De momento vamos a regresar los métodos set para que se puedan modificar.
Posterior a la creación del objeto.
Los valores de ancho y alto.
Bien, por último, vamos a mencionar ahora el método MRO Mesos Resolution Order.
Si lo mandamos a llamar a partir de la clase Quadrado, el método MRO.
Vamos a observar algunas diferencias.
Podemos, cvar el siguiente orden tenemos la clase cuadrado.
Posteriormente la clase figura geométrica, pero ahora la siguiente clase es la clase abecé.
Abstract Veus class, ya que recordemos que esta es la clase padre de la clase de figura geométrica.
Así que después de la clase figura geométrica se encuentra en la clase a veces posteriormente se encuentra
en la clase de color y finalmente la clase Object.
Así que ahora se modifica el orden de resolución de nuestras clases.
Este es el nuevo orden de jerarquía de clases.
Cuando estamos trabajando con herencia múltiple en Python.
Así que solamente es un pequeño comentario, se modifica.
El mesos.
Resolución Order.
Debido a que nuestra clase de figura geométrica hemos incluido una nueva clase padre, la clase ARP-SAPC,
'''

from Cuadrado import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Rectangulo import Rectangulo

# No se puede instanciar una clase abstracta
# figura = FiguraGeometrica()

print('Creación Objeto cuadrado'.center(50,'-'))
cuadrado1 = Cuadrado(lado=5, color='rojo')
cuadrado1.alto = 9
cuadrado1.ancho = 9
print(f'Cálculo área cuadrado 12xxxx: {cuadrado1.calcular_area()}')
print(cuadrado1)

print('Creación Objeto rectángulo'.center(50,'-'))
rectangulo1 = Rectangulo(ancho=9, alto=8, color='verde')
rectangulo1.ancho = 15
print(f'Cálculo área rectángulo 18xxx: {rectangulo1.calcular_area()}')
print(rectangulo1)

#Method Resolution Order
print(Cuadrado.mro())