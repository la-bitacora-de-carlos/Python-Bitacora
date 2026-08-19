"""
==============================================================================
GUÍA DE ESTUDIO: ESTRUCTURAS CONDICIONALES EN PYTHON (if, elif, else)
==============================================================================
Las estructuras condicionales permiten ejecutar bloques de código específicos 
según si una condición evalúa como `True` o `False`.

Puntos clave:
------------------------------------------------------------------------------
1. Indentación (Sangría): En Python es OBLIGATORIA (estándar PEP 8: 4 espacios).
   Define visualmente qué líneas pertenecen a cada bloque.
2. if: Se ejecuta únicamente si su condición es True.
3. elif: (Else If) Evalúa una nueva condición si la previa resultó False.
4. else: Se ejecuta solo si NINGUNA de las condiciones anteriores fue True.
==============================================================================
"""

# ============================================================================
# 1. CONDICIONAL BÁSICO (if - else) Y CONTROL DE INDENTACIÓN
# ============================================================================
edad = 19

print("--- EVALUACIÓN BÁSICA (if / else) ---")
if edad >= 18:
    print("Puedes pasar")
    print("Forma parte del if (indentado a 4 espacios)")
else:
    print("No puedes pasar")
    print("Forma parte del else")

# Código fuera del bloque condicional
print("No forma parte de ninguna condición (se ejecuta siempre)\n")


# ============================================================================
# 2. AMPLIACIÓN: MÚLTIPLES CONDICIONES (if - elif - else)
# ============================================================================
# Se evalúan en orden descendente. En cuanto una se cumple, las demás se ignoran.

ingreso_mensual = 25000

print("--- EVALUACIÓN MÚLTIPLE (elif) ---")
if ingreso_mensual > 50000:
    print("Categoría: Ingreso alto")
elif ingreso_mensual >= 20000:
    print("Categoría: Ingreso medio")
elif ingreso_mensual > 0:
    print("Categoría: Ingreso básico")
else:
    print("Categoría: Sin ingresos registrados")
print()


# ============================================================================
# 3. AMPLIACIÓN: CONDICIONES COMPUESTAS (and, or, not)
# ============================================================================
tiene_identificacion = True
edad_cliente = 20

print("--- CONDICIONES COMBINADAS CON OPERADORES LÓGICOS ---")
if edad_cliente >= 18 and tiene_identificacion:
    print("Acceso concedido: Cumple con la edad y tiene identificación.")
else:
    print("Acceso denegado: Falta alguno de los requisitos.")
print()


# ============================================================================
# 4. AMPLIACIÓN: OPERADOR TERNARIO (Condicional simple en una línea)
# ============================================================================
# Sintaxis: [valor_si_true] if [condicion] else [valor_si_false]

estado_acceso = "Permitido" if edad >= 18 else "Denegado"

print("--- OPERADOR TERNARIO ---")
print(f"Estado de acceso rápido: {estado_acceso}")