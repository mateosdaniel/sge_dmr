# 10. Concatenación de listas de caracteres
# Dadas dos listas de caracteres, usa reduce para concatenarlas en una sola lista sin utilizar + o métodos de concatenación.

from functools import reduce

lista1 = ['a', 'b', 'c']
lista2 = ['x', 'y', 'z']

res = reduce (lambda a, b: [*a, *b], [lista1, lista2])
print(res)