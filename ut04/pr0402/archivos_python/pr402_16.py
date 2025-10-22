# 16. Contar la longitud de palabra más larga
# Escribe un programa que reciba una cadena y devuelva la longitud de la palabra más larga
text = input("Introcude varias palabras: ")
palabras = text.split()
longitud_maxima = 0
for palabra in palabras:
    if len(palabra) > longitud_maxima:
        longitud_maxima = len(palabra)
print(longitud_maxima)