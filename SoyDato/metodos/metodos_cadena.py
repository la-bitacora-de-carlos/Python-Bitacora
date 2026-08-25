"""
==============================================================================
GUÍA DE ESTUDIO: MÉTODOS Y FUNCIONES PARA CADENAS (STRINGS) EN PYTHON
==============================================================================
En Python, las cadenas son objetos inmutables. Los métodos de cadenas no 
modifican la cadena original, sino que devuelven una nueva cadena transformada.

Diferencia clave:
------------------------------------------------------------------------------
* Funciones nativas: Se llaman pasando la cadena como argumento -> len(cadena)
* Métodos del objeto: Se llaman con notación de punto -> cadena.upper()
==============================================================================
"""

cadena1 = "hola soy carlos"
cadena2 = "Bienvenido_a_este_curso_de_python3"
cadena_num = "12345"
cadena_solo_letras = "Hola"


# ============================================================================
# 1. INSPECCIÓN Y LONGITUD (Funciones nativas)
# ============================================================================
print("--- INSPECCIÓN Y LONGITUD ---")
# len(): Devuelve la cantidad de caracteres de la cadena
print(f"Longitud de cadena2: {len(cadena2)}")

# dir(): Muestra todos los métodos y atributos disponibles para el objeto
print("Atributos y métodos disponibles (dir):", dir(cadena1)[:5], "...") 
print()


# ============================================================================
# 2. TRANSFORMACIÓN DE FORMATO (MAYÚSCULAS Y MINÚSCULAS)
# ============================================================================
print("--- FORMATO Y MAYÚSCULAS/MINÚSCULAS ---")
print("upper()      :", cadena1.upper())       # HOLA SOY CARLOS
print("lower()      :", cadena1.lower())       # hola soy carlos
print("capitalize() :", cadena1.capitalize())  # Hola soy carlos (solo 1° letra del texto)
print("title()      :", cadena1.title())       # Hola Soy Carlos (1° letra de cada palabra)
print()


# ============================================================================
# 3. BÚSQUEDA Y CONTEO DE ELEMENTOS
# ============================================================================
print("--- BÚSQUEDA Y CONTEO ---")
# find(): Devuelve el índice de la 1° coincidencia. Si no existe, devuelve -1
print("find('carlos') :", cadena1.find('carlos'))  # Índice 9
print("find('python') :", cadena1.find('python'))  # -1 (no existe)

# index(): Similar a find, pero si no encuentra nada LANZA UNA EXCEPCIÓN (ValueError)
print("index('c')     :", cadena1.index('c'))     # Índice 9

# count(): Cuenta cuántas veces se repite una subcadena
print("count('o')     :", cadena2.count('o'))
print()


# ============================================================================
# 4. VALIDACIÓN DE CONTENIDO (Métodos is...)
# ============================================================================
print("--- VALIDACIÓN DE CONTENIDO ---")
# isnumeric(): True si todos los caracteres son dígitos numéricos
print("isnumeric() '12345' :", cadena_num.isnumeric())  # True
print("isnumeric() cadena1 :", cadena1.isnumeric())     # False

# isalpha(): True si TODOS los caracteres son letras (sin espacios, números ni guiones)
print("isalpha() 'Hola'    :", cadena_solo_letras.isalpha())  # True
print("isalpha() cadena2   :", cadena2.isalpha())            # False (tiene '_' y '3')

# startswith() / endswith(): Verifican inicio o final de cadena
print("startswith('Bienvenido') :", cadena2.startswith('Bienvenido'))  # True
print("endswith('3')            :", cadena2.endswith('3'))             # True
print()


# ============================================================================
# 5. REEMPLAZO, LIMPIEZA Y SEPARACIÓN (MANIPULACIÓN)
# ============================================================================
print("--- MANIPULACIÓN Y SEPARACIÓN ---")
# replace(): Reemplaza un fragmento de texto por otro
cadena_modificada = cadena2.replace('3', '3.15')
print("replace('3', '3.15') :", cadena_modificada)

# split(): Divide una cadena en una LISTA según el separador indicado
lista_palabras = cadena2.split('_')
print("split('_')           :", lista_palabras)  # ['Bienvenido', 'a', 'este', ...]

# strip() [Ampliación]: Elimina espacios en blanco al inicio y al final
cadena_espacios = "   Hola Mundo   "
print("strip()              :", f"'{cadena_espacios.strip()}'")

# join() [Ampliación]: Une los elementos de una lista en un string mediante un separador
lista_unir = ['Python', 'es', 'genial']
print("join(' ')            :", " ".join(lista_unir))