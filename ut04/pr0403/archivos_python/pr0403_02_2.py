# Contar elementos específicos: 
# Dada una lista de palabras, permite al usuario ingresar una palabra y cuenta cuántas veces aparece en la lista.

palabra = input("Escribe una palabra: ")
palabras = ["palabra1", "palabra1", "palabra1", "palabra1", "palabra1", "palabra1", "palabra2", "palabra2" ]
cantidad = palabras.count(palabra)

print(f"La palabra '{palabra}' aparece {cantidad} veces.")