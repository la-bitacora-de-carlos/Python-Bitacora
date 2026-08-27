"""
==============================================================================
GUÍA DE ESTUDIO: MÉTODOS PARA DICCIONARIOS EN PYTHON (dict)
==============================================================================
Los diccionarios son estructuras de datos mutable organizadas en pares 
`clave: valor`. 

Puntos clave:
------------------------------------------------------------------------------
1. Claves únicas: No pueden repetirse.
2. Acceso por clave: Se accede mediante su clave, no por un índice numérico.
3. Métodos de lectura segura: `.get()` evita que el programa falle si una 
   clave no existe.
==============================================================================
"""

diccionario = {
    "nombre": "Carlos",
    "apellido": "Morales",
    "subs": "1000000"
}

print("--- DICCIONARIO INICIAL ---")
print("Diccionario completo:", diccionario)
print()


# ============================================================================
# 1. INSPECCIÓN Y LECTURA DE ELEMENTOS
# ============================================================================
print("--- LECTURA Y OBTENCIÓN DE DATOS ---")

# keys(): Devuelve un objeto iterable con todas las claves del diccionario
claves = diccionario.keys()
print(f"Claves (.keys()): {claves}")

# get(): Devuelve el valor de la clave especificada. 
# Si la clave NO existe, devuelve None (o un valor predeterminado) en lugar de un KeyError.
valor_subs = diccionario.get("subs")
valor_inexistente = diccionario.get("edad", "Clave no encontrada")

print(f"Valor de 'subs' (.get()): {valor_subs}")
print(f"Búsqueda segura (.get()): {valor_inexistente}")
print()


# ============================================================================
# 2. ELIMINACIÓN DE ELEMENTOS
# ============================================================================
print("--- ELIMINACIÓN DE DATOS ---")

# pop(): Elimina la clave especificada y DEVUELVE su valor asociado
elemento_eliminado = diccionario.pop("subs")
print(f"Elemento eliminado con .pop('subs'): {elemento_eliminado}")
print("Diccionario tras pop:", diccionario)

# clear(): Elimina TODOS los pares clave-valor dejando el diccionario vacío
# diccionario.clear()
print()


# ============================================================================
# 3. VISTAS E ITERACIÓN (items)
# ============================================================================
print("--- DICCIONARIO COMO TUPLAS (items) ---")

# items(): Devuelve una lista/vista de tuplas donde cada elemento es (clave, valor)
# Es el método estándar para iterar diccionarios con bucles for.
items_diccionario = diccionario.items()
print(f"Estructura (.items()): {items_diccionario}")
print()


# ============================================================================
# 4. AMPLIACIÓN: MÉTODOS ÚTILES (values y update)
# ============================================================================
print("--- AMPLIACIÓN DE MÉTODOS ---")

# values(): Devuelve solo los valores del diccionario (sin las claves)
print(f"Valores (.values()): {list(diccionario.values())}")

# update(): Actualiza el diccionario agregando nuevos pares o modificando los existentes
diccionario.update({
    "profesion": "Programador",
    "nombre": "Carlos Jose"  # Sobrescribe el valor de 'nombre'
})
print("Diccionario tras .update():", diccionario)