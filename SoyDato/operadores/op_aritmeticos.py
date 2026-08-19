"""
==============================================================================
GUÍA DE ESTUDIO: OPERADORES ARITMÉTICOS EN PYTHON
==============================================================================
Los operadores aritméticos realizan operaciones matemáticas estándar sobre
valores numéricos (enteros `int` y flotantes `float`).

Resumen rápido de operadores:
------------------------------------------------------------------------------
Operador | Nombre               | Ejemplo   | Resultado
------------------------------------------------------------------------------
   +     | Suma                 | 12 + 5    | 17
   -     | Resta                | 12 - 5    | 7
   *     | Multiplicación       | 5 * 5     | 25
   /     | División (flotante)  | 12 / 5    | 2.4 (siempre float)
   **    | Exponente / Potencia | 12 ** 2   | 144
   //    | División entera/baja | 12 // 5   | 2 (descarta decimales)
   %     | Módulo (Resto)       | 12 % 5    | 2 (residuo de la división)
------------------------------------------------------------------------------
==============================================================================
"""

# ============================================================================
# 1. SUMA Y RESTA
# ============================================================================
suma = 12 + 5
resta = 12 - 5

print("--- SUMA Y RESTA ---")
print(f"Suma (12 + 5): {suma}")
print(f"Resta (12 - 5): {resta}")
print()


# ============================================================================
# 2. MULTIPLICACIÓN Y DIVISIÓN
# ============================================================================
multiplicacion = 5 * 5

# La división (/) SIEMPRE devuelve un número de tipo flotante (float)
division = 12 / 5

print("--- MULTIPLICACIÓN Y DIVISIÓN ---")
print(f"Multiplicación (5 * 5): {multiplicacion}")
print(f"División (12 / 5): {division}")

# Verificación del tipo de dato que retorna la división
tipo_division = type(division)
print(f"Tipo de dato de la división: {tipo_division}")  # <class 'float'>
print()


# ============================================================================
# 3. POTENCIACIÓN (EXPONENTE)
# ============================================================================
exponente = 12 ** 2  # 12 elevado al cuadrado

print("--- POTENCIACIÓN ---")
print(f"Exponente (12 ** 2): {exponente}")
print()


# ============================================================================
# 4. DIVISIÓN ENTERA (DIVISIÓN BAJA) Y MÓDULO (RESTO)
# ============================================================================
# La división entera (//) devuelve el cociente redondeado hacia abajo (sin decimales)
division_baja = 12 // 5

# El módulo (%) devuelve el residuo/resto que queda de la división
resto = 12 % 5

print("--- DIVISIÓN ENTERA Y MÓDULO ---")
print(f"División entera (12 // 5): {division_baja}")  # Resultado: 2
print(f"Módulo / Resto (12 % 5): {resto}")             # Resultado: 2
print()


# ============================================================================
# 5. AMPLIACIÓN: JERARQUÍA / PRECEDENCIA DE OPERADORES (PEMDAS)
# ============================================================================
# Regla de prioridad en evaluaciones matemáticas:
# 1. Paréntesis ()
# 2. Exponentes **
# 3. Multiplicación, División, Módulo, División entera (*, /, %, //)
# 4. Suma y Resta (+, -)

operacion_combinada = 12 + 5 * 2 ** 2
print("--- PRECEDENCIA DE OPERADORES ---")
print(f"12 + 5 * 2 ** 2 = {operacion_combinada}")  # Primero 2**2 = 4, luego 5*4 = 20, finalmente 12+20 = 32

operacion_con_parentesis = (12 + 5) * 2
print(f"(12 + 5) * 2 = {operacion_con_parentesis}")  # Primero (12+5) = 17, luego 17*2 = 34