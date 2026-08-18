"""
==============================================================================
GUÍA DE ESTUDIO: TIPOS DE DATOS COMPUESTOS EN PYTHON
==============================================================================
Los tipos de datos compuestos (o estructuras de datos) permiten agrupar 
múltiples valores bajo una sola variable.

Resumen rápido de características:
------------------------------------------------------------------------------
Estructura   | Ordenada | Mutable | Permite Duplicados | Acceso por
------------------------------------------------------------------------------
List         | Sí       | Sí      | Sí                 | Índice numérico
Tuple        | Sí       | No      | Sí                 | Índice numérico
Set          | No       | Sí*     | No                 | No indexado
Dict         | Sí (3.7+) | Sí      | Claves Únicas      | Clave (Key)
------------------------------------------------------------------------------
* Los elementos individuales de un Set no se modifican por índice, pero se
  pueden agregar o eliminar elementos del conjunto general.
==============================================================================
"""

# ============================================================================
# 1. LISTAS (list)
# ============================================================================
# Estructuras ordenadas y mutables. Se definen con corchetes [].

listas = ['Carlos Morales', 'Labitacoradecarlosmorales', True, 5.5]
print("--- LISTAS ---")
print("Lista completa:", listas)

# Acceso por índices (comienzan en 0)
print("Primer elemento (índice 0):", listas[0])
print("Último elemento (índice -1):", listas[-1])

# Modificación (Las listas SÍ son mutables)
listas[0] = 'Carlos'
print("Lista modificada:", listas)

# Operaciones comunes ampliadas:
listas.append('Nuevo Dato')      # Agregar al final
listas.pop(2)                     # Eliminar elemento en el índice 2 (True)
sublista = listas[0:2]            # Slicing (sublista desde índice 0 hasta 1)
print("Sublista (Slicing 0:2):", sublista)
print()


# ============================================================================
# 2. TUPLAS (tuple)
# ============================================================================
# Estructuras ordenadas e INMUTABLES. Se definen con paréntesis ().
# Se utilizan cuando los datos no deben cambiar a lo largo del programa.

tupla = ('Carlos Morales', 'Labitacoradecarlosmorales', True, 5.5)
print("--- TUPLAS ---")
print("Tupla completa:", tupla)
print("Primer elemento:", tupla[0])

# Intento de modificación:
# tupla[0] = "Jose"  # TypeError: 'tuple' object does not support item assignment

# Desempaquetado de tuplas (Unpacking):
nombre, canal, activo, nota = tupla
print(f"Desempaquetado -> Nombre: {nombre}, Canal: {canal}")
print()


# ============================================================================
# 3. CONJUNTOS (set)
# ============================================================================
# Colección de elementos NO ORDENADOS y SIN DUPLICADOS.
# Se definen con llaves {}. No se puede acceder por índice.

conjunto = {'Carlos Morales', 'Labitacoradecarlosmorales', True, 5.5, 'Carlos Morales'}
print("--- CONJUNTOS (SET) ---")
# El elemento duplicado 'Carlos Morales' se elimina automáticamente
print("Conjunto (duplicados omitidos):", conjunto)

# Intento de acceso por índice:
# print(conjunto[0]) # TypeError: 'set' object is not subscriptable

# Operaciones comunes ampliadas:
conjunto.add('Python')            # Agregar nuevo elemento
conjunto.discard('Carlos Morales') # Eliminar un elemento existente
print("Comprobación de pertenencia ('Python' in conjunto):", 'Python' in conjunto)
print("Conjunto actualizado:", conjunto)
print()


# ============================================================================
# 4. DICCIONARIOS (dict)
# ============================================================================
# Estructura de pares clave: valor (similar a formato JSON).
# Las claves deben ser únicas e inmutables (strings, números, tuplas).

diccionario = {
    'nombre': 'Carlos Morales',
    'canal': 'labitacoradecaros',
    'altura': 5.5,
    'datosduplicado': "Carlos Morales"  # Los valores sí pueden duplicarse
}

print("--- DICCIONARIOS ---")
print("Diccionario completo:", diccionario)

# Acceso a valores por su clave
print("Valor de 'canal':", diccionario['canal'])

# Uso de .get() (Método seguro que no arroja error si la clave no existe)
print("Uso de .get():", diccionario.get('edad', 'Clave no encontrada'))

# Modificación y adición de pares clave:valor
diccionario['nombre'] = 'Carlos J. Morales'  # Modificar valor existente
diccionario['lenguaje'] = 'Python'           # Agregar nueva clave:valor
print("Diccionario actualizado:", diccionario)

# Obtener claves y valores por separado
print("Claves:", list(diccionario.keys()))
print("Valores:", list(diccionario.values()))