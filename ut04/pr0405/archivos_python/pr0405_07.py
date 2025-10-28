# 7. Frecuencia de palabras
# Dado un texto, crea una función que use map y reduce para obtener la frecuencia de cada palabra. Ignora las mayúsculas y minúsculas y supón que no hay símbolos de puntuación.

from functools import reduce

texto = "Hola hola mundo mundo cruel"
texto_lower = texto.lower()
lista_palabras = texto_lower.split(" ")

def agregar_frecuencia(dic, palabra):
    dic[palabra] = dic.get(palabra, 0) + 1
    return dic

res = reduce(agregar_frecuencia, lista_palabras, {})
print(res)