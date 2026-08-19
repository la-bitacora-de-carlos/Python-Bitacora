"""
==============================================================================
GUÍA DE ESTUDIO: OPERADORES DE COMPARACIÓN EN PYTHON
==============================================================================
Los operadores de comparación evaluán la relación entre dos valores y 
siempre devuelven un tipo de dato booleano: `True` (Verdadero) o `False` (Falso).

Resumen rápido de operadores:
------------------------------------------------------------------------------
Operador | Nombre              | Ejemplo  | Resultado
------------------------------------------------------------------------------
   ==    | Igual que           | 5 == 6   | False
   !=    | Distinto de         | 5 != 6   | True
   >     | Mayor que           | 5 > 6    | False
   <     | Menor que           | 5 < 6    | True
   >=    | Mayor o igual que   | 5 >= 6   | False
   <=    | Menor o igual que   | 5 <= 6   | True
------------------------------------------------------------------------------
==============================================================================
"""

# ============================================================================
# 1. OPERADORES BÁSICOS DE COMPARACIÓN
# ============================================================================
igual_que = 5 == 6       # False
distinto_de = 5 != 6     # True
mayor_que = 5 > 6        # False
menor_que = 5 < 6        # True
mayor_o_igual = 5 >= 6   # False
menor_o_igual = 5 <= 6   # True

print("--- RESULTADOS DE LAS COMPARACIONES ---")
print(f"5 == 6 : {igual_que}")
print(f"5 != 6 : {distinto_de}")
print(f"5 > 6  : {mayor_que}")
print(f"5 < 6  : {menor_que}")
print(f"5 >= 6 : {mayor_o_igual}")
print(f"5 <= 6 : {menor_o_igual}")
print()


# ============================================================================
# 2. VERIFICACIÓN DEL TIPO DE DATO DEVUELTO
# ============================================================================
# Toda comparación produce un dato de tipo 'bool' (booleano)
es_booleano = type(igual_que)
print("--- TIPO DE DATO RESULTANTE ---")
print(f"Tipo de dato de 'igual_que': {es_booleano}")  # <class 'bool'>
print()


# ============================================================================
# 3. AMPLIACIÓN: COMPARACIÓN DE CADENAS DE TEXTO (STRINGS)
# ============================================================================
# Las cadenas se comparan considerando mayúsculas y minúsculas (Case Sensitive)

usuario_registrado = "Carlos"
usuario_ingresado = "carlos"

son_iguales = usuario_registrado == usuario_ingresado
print("--- COMPARACIÓN DE TEXTO ---")
print(f"'Carlos' == 'carlos': {son_iguales}")  # False debido a la mayúscula
print()


# ============================================================================
# 4. AMPLIACIÓN: CASO PRÁCTICO (VALIDACIÓN DE CONDICIÓN)
# ============================================================================
# Ejemplo común: verificar un límite o requerimiento de edad

edad_usuario = 20
edad_minima = 18

es_mayor_de_edad = edad_usuario >= edad_minima
print("--- CASO PRÁCTICO ---")
print(f"¿Edad ({edad_usuario}) es suficiente para ingresar (>= {edad_minima})?: {es_mayor_de_edad}")