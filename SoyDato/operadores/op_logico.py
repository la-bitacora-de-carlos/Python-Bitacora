"""
==============================================================================
GUÍA DE ESTUDIO: OPERADORES LÓGICOS EN PYTHON (and, or, not)
==============================================================================
Los operadores lógicos evalúan condiciones booleanas y permiten combinar 
múltiples expresiones.

Diferencia importante:
------------------------------------------------------------------------------
Lógicos (Uso correcto aquí) | Bitwise (A nivel de bits)
------------------------------------------------------------------------------
   and                      |   &
   or                       |   |
   not                      |   ~
------------------------------------------------------------------------------
==============================================================================
"""

# ============================================================================
# 1. OPERADOR LÓGICO AND (Y)
# ============================================================================
# Retorna True ÚNICAMENTE si AMBAS condiciones son True.

r_and1 = True and True    # True
r_and2 = False and True   # False
r_and3 = True and False   # False
r_and4 = False and False  # False

print("--- TABLA DE VERDAD: AND ---")
print(f"True  and True  : {r_and1}")
print(f"False and True  : {r_and2}")
print(f"True  and False : {r_and3}")
print(f"False and False : {r_and4}")
print()


# ============================================================================
# 2. OPERADOR LÓGICO OR (O)
# ============================================================================
# Retorna True si AL MENOS UNA de las condiciones es True.

r_or1 = True or True     # True
r_or2 = False or True    # True
r_or3 = True or False    # True
r_or4 = False or False   # False

print("--- TABLA DE VERDAD: OR ---")
print(f"True  or True  : {r_or1}")
print(f"False or True  : {r_or2}")
print(f"True  or False : {r_or3}")
print(f"False or False : {r_or4}")
print()


# ============================================================================
# 3. OPERADOR LÓGICO NOT (NEGACIÓN)
# ============================================================================
# Invierte el valor booleano: de True pasa a False y viceversa.

r_not1 = not True   # False
r_not2 = not False  # True

print("--- NEGACIÓN: NOT ---")
print(f"not True  : {r_not1}")
print(f"not False : {r_not2}")
print()


# ============================================================================
# 4. AMPLIACIÓN: CASO PRÁCTICO COMBINADO
# ============================================================================
# Evaluación de condiciones reales mezclando operadores de comparación y lógicos

edad = 25
tiene_licencia = True
tiene_multas_pendientes = False

# Puede conducir si es mayor de edad, tiene licencia Y NO tiene multas
puede_conducir = (edad >= 18) and tiene_licencia and (not tiene_multas_pendientes)

print("--- CASO PRÁCTICO COMBINADO ---")
print(f"¿Puede conducir el usuario?: {puede_conducir}")  # True