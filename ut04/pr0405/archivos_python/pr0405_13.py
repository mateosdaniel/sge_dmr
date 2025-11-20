# 13. Pipe de transformaciones de listas
# Implementa una función que tome una lista de funciones y una lista de números, y aplique cada función de la lista en secuencia sobre la lista de números usando reduce.

from functools import reduce

funciones = [lambda x: x*2, lambda x: x+3, lambda x: x-1]
numeros = [1, 2, 3]

# Función para aplicar una función sobre toda la lista
def aplicar_lista(func, lista):
    return [func(x) for x in lista]

# Reduce para aplicar todas las funciones en secuencia
resultado = reduce(lambda acc, f: aplicar_lista(f, acc), funciones, numeros)

print(resultado)
