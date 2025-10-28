# 3. Suma acumulativa
# Utiliza reduce para obtener la suma acumulativa de una lista de números.

from functools import reduce

numeros = [1, 2, 3, 4, 5]

def sumar(n , acum):
    return n + acum

res = reduce(sumar, numeros, 0)
print(res)
