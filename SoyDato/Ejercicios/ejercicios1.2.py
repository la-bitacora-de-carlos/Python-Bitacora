frase = input('Decime una frase y te calculo cuando duraria sin tengo que decirla: ')

palabras_separadas = frase.split(' ')
candidad_de_palabras= len(palabras_separadas)

print(f"Dijiste {candidad_de_palabras} palabras  y tardarias {candidad_de_palabras /2} segundos en decirlo ")
print(f"Yo me tardaria {candidad_de_palabras/2*1.3} segundos en decirlo" )

if candidad_de_palabras > 20:
    print("Tan poco te pedi un testamento")