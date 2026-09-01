
promedio_minimo = 2.5
promedio = 4
promedio_maximo = 7

tiempo_este_cursos = 1.5

print(f" diferencia entre el curso actual {tiempo_este_cursos} y el mas rapido de los otros curso {promedio_maximo} es igual a : {promedio_maximo - tiempo_este_cursos}")

print(f" diferencia entre el curso actual {tiempo_este_cursos} y el mas lento de los otros curso {promedio_minimo} es igual a : {promedio_minimo - tiempo_este_cursos}")

print(f" diferencia entre el curso actual {tiempo_este_cursos} y el promedio de los otros curso {promedio} es igual a : {promedio - tiempo_este_cursos}")

videos_sin_edicion_otros = 5
videos_sin_edicion = 3.5
Horas_reducidas_este = videos_sin_edicion - tiempo_este_cursos
Horas_reducidas_otros = videos_sin_edicion_otros - promedio
print(f"Horas que se reduce con edicion en este curso es: {Horas_reducidas_este}")
print(f"Horas que se reduce con edicion en otros cursos es: {Horas_reducidas_otros}")

horas_equivalente_este = (10 * promedio) / tiempo_este_cursos
horas_equivalente_otros = (10*tiempo_este_cursos) / promedio

print(f'Ver 10 horas de este curso equivale a {horas_equivalente_este} horas de otros')
print(f'Ver 10 horas de otros curso equivale a {horas_equivalente_otros} horas de este')