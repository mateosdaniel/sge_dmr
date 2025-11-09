# 13. Pipe de transformaciones de listas
# Implementa una función que tome una lista de funciones y una lista de números, y aplique cada función de la lista en secuencia sobre la lista de números usando reduce.

from functools import reduce

funciones = [lambda x: x*2, lambda x: x+3, lambda x: x-1]
numeros = [1, 2, 3]

for i in range(len(funciones)):
    res = reduce(funciones[i], numeros, 0)
    print (res)