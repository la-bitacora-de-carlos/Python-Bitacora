"""
==============================================================================
GUÍA DE ESTUDIO: MÉTODOS PARA LISTAS EN PYTHON
==============================================================================
Las listas son colecciones ORDENADAS y MUTABLES. A diferencia de los métodos
de cadenas (que devuelven un nuevo string), la mayoría de los métodos de listas
MODIFICAN la lista original directamente en memoria (operación in-place).

Diferencia importante:
------------------------------------------------------------------------------
* lista.sort()   -> Modifica la lista original (devuelve None).
* sorted(lista)  -> Devuelve una NUEVA lista ordenada sin alterar la original.
==============================================================================
"""

# Creación de lista usando la función constructora list() pasando una tupla
lista = list((37, 80, 34, 37))

print("--- LISTA INICIAL Y LONGITUD ---")
print("Lista original:", lista)
print("Cantidad de elementos (len):", len(lista))
print()


# ============================================================================
# 1. MÉTODOS PARA AGREGAR ELEMENTOS (AÑADIR)
# ============================================================================
print("--- AGREGAR ELEMENTOS ---")
# append(): Agrega UN solo elemento al FINAL de la lista
lista.append(65)
print("append(65)            :", lista)

# insert(): Agrega un elemento en un ÍNDICE ESPECÍFICO (posición, valor)
lista.insert(2, 55)  # En el índice 2 coloca el valor 55
print("insert(2, 55)         :", lista)

# extend(): Agrega MÚLTIPLES elementos al final pasándole una lista/iterable
lista.extend([140, 2026])
print("extend([140, 2026])   :", lista)
print()


# ============================================================================
# 2. MÉTODOS PARA ELIMINAR ELEMENTOS
# ============================================================================
print("--- ELIMINAR ELEMENTOS ---")
# pop(): Elimina y devuelve el elemento en el índice indicado.
# Si usas -1, elimina el ÚLTIMO elemento.
elemento_eliminado_0 = lista.pop(0)   # Elimina el primer elemento
elemento_eliminado_ult = lista.pop(-1) # Elimina el último elemento
print(f"pop(0) eliminó ({elemento_eliminado_0}) y pop(-1) eliminó ({elemento_eliminado_ult})")
print("Lista tras pop        :", lista)

# remove(): Elimina la PRIMERA coincidencia del VALOR especificado
lista.remove(34)
print("remove(34)            :", lista)

# clear(): Elimina TODOS los elementos dejando la lista vacía
# lista.clear()
print()


# ============================================================================
# 3. ORDENAMIENTO Y INVERSIÓN (OPERACIONES IN-PLACE)
# ============================================================================
print("--- ORDENAMIENTO E INVERSIÓN ---")
# sort(): Ordena de menor a mayor (Ascendente)
lista.sort()
print("sort() Ascendente     :", lista)

# sort(reverse=True): Ordena de mayor a menor (Descendente)
lista.sort(reverse=True)
print("sort(reverse=True)    :", lista)

# reverse(): Invierte el orden actual de los elementos (sin evaluar cuál es mayor o menor)
lista.reverse()
print("reverse()             :", lista)
print()


# ============================================================================
# 4. AMPLIACIÓN: BÚSQUEDA Y CONTEO
# ============================================================================
print("--- BÚSQUEDA Y CONTEO ---")
# count(): Cuenta cuántas veces aparece un valor en la lista
print("count(37)             :", lista.count(37))

# index(): Devuelve la posición (índice) del valor buscado
print("index(80)            :", lista.index(80))