"""
DECLARACIÓN Y ASIGNACIÓN DE VARIABLES

Las variables son espacios lógicos de memoria utilizados para almacenar datos.
Su valor puede cambiar durante la ejecución del programa.

Python es un lenguaje de tipado dinámico, por lo que no es necesario
especificar el tipo de dato al crear una variable.
"""

a = 5
a = 6

print(a)


"""
CREACIÓN (ASIGNACIÓN) DE VARIABLES

Una variable se crea al asignarle un valor por primera vez.
"""

nombre = "Carlos Morales"
apellidos = "Morales De Jesus"


"""
MOSTRAR EL CONTENIDO DE UNA VARIABLE
"""

print(nombre)


"""
REASIGNACIÓN O REDEFINICIÓN DEL VALOR DE UNA VARIABLE

Una variable puede recibir un nuevo valor durante la ejecución
del programa.
"""

nombre = "Carlos Jose"

print(nombre)


"""
CONCATENACIÓN DE VARIABLES

Consiste en unir cadenas de texto y variables para formar una
sola salida.
"""

# Usando f-string (recomendado)
print(f"Mi nombre es {nombre} y mi apellido es {apellidos}")

# Usando el operador +
print("Mi nombre es: " + nombre + " y mi apellido es: " + apellidos)


"""
ELIMINAR UNA VARIABLE

La palabra reservada 'del' elimina una variable del espacio
de nombres actual.

Si se intenta acceder a la variable después de eliminarla,
Python generará un NameError.
"""

nombres = nombre

# Comentario de una sola línea
del nombre

print("Mi nombre es: " + nombres + " y mi apellido es: " + apellidos)


"""
OPERADORES DE PERTENENCIA: in y not in

Permiten verificar si un valor existe dentro de una cadena,
lista, tupla o cualquier colección iterable.
"""

print("Jose" in nombres)
print("jose" not in nombres)


"""
PYTHON ES CASE SENSITIVE

Python diferencia entre mayúsculas y minúsculas.

Ejemplos:
nombre != Nombre
jose != Jose
"""


"""
CONVENCIONES PARA NOMBRAR VARIABLES
"""

# PascalCase (generalmente usado para clases)
NombreCompletoConApellido = "Carlos Morales"

# snake_case (convención recomendada para variables y funciones)
nombre_completo = "Carlos Morales"


"""
BUENAS PRÁCTICAS PARA NOMBRAR VARIABLES

✅ Utilizar nombres descriptivos.
✅ Evitar caracteres especiales.
✅ No utilizar palabras reservadas de Python.
✅ Seguir la convención snake_case.
"""

edad = 30
correo_electronico = "correo@dominio.com"
salario_mensual = 25000


