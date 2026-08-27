"""
==============================================================================
GUÍA DE ESTUDIO: ENTRADA DE DATOS CON input() EN PYTHON
==============================================================================
La función `input()` permite pausar la ejecución del programa para que el 
usuario ingrese información desde la consola/terminal.

Reglas clave:
------------------------------------------------------------------------------
1. Tipo de retorno único: `input()` SIEMPRE retorna un valor de tipo string (`str`).
2. Conversión de tipos (Casting): Para trabajar con números en operaciones 
   matemáticas, es obligatorio envolver el `input()` dentro de `int()` o `float()`.
3. Manejo de errores: Si el usuario ingresa un texto no numérico al realizar 
   un casting directo, Python arrojará un error de tipo `ValueError`.
==============================================================================
"""

# ============================================================================
# 1. ENTRADA DE TEXTO (STRING)
# ============================================================================
# No requiere ninguna conversión adicional.
nombre = input("¿Cuál es tu nombre?: ")

print("--- REGISTRO DE TEXTO ---")
print(f"Su nombre es: {nombre}")
print(f"Tipo de dato guardado: {type(nombre)}")  # <class 'str'>
print()


# ============================================================================
# 2. ENTRADA DE NÚMEROS ENTEROS (INT)
# ============================================================================
# Convertimos directamente la salida del input a int.
edad = int(input("Dame tu edad: "))

print("--- REGISTRO DE ENTEROS ---")
print(f"Mi edad es: {edad}")
print(f"Tipo de dato guardado: {type(edad)}")  # <class 'int'>

# Ejemplo práctico: Operación con el número ingresado
print(f"El próximo año tendrás: {edad + 1} años")
print()


# ============================================================================
# 3. ENTRADA DE NÚMEROS DECIMALES (FLOAT)
# ============================================================================
# Convertimos la salida del input a float. (Nota: Usar punto '.' para decimales)
estatura = float(input("Dame tu estatura (ejemplo 1.75): "))

print("--- REGISTRO DE FLOTANTES ---")
print(f"Mi estatura es: {estatura} metros")
print(f"Tipo de dato guardado: {type(estatura)}")  # <class 'float'>
print()


# ============================================================================
# 4. AMPLIACIÓN: VALIDACIÓN BÁSICA DE ENTRADA (Manejo de Errores / try-except)
# ============================================================================
# Permite prevenir que el programa se detenga abruptamente si el usuario
# ingresa letras en lugar de un número.

print("--- VALIDACIÓN DE ENTRADA SEGURA ---")
entrada_usuario = input("Ingresa un número entero para validar: ")

if entrada_usuario.isnumeric():
    numero_validado = int(entrada_usuario)
    print(f"¡Éxito! Número procesado correctamente: {numero_validado}")
else:
    print("Error: El dato ingresado no es un número entero válido.")