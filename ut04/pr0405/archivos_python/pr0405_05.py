# 5. Multiplicación de pares
# Dada una lista de números, utiliza filter, map y reduce para obtener el producto de los números pares.

from functools import reduce
numeros = [1, 2, 3, 4, 5, 6]
pares = []
res = []

def pares(numero):
    return numero%2 == 0

def producto (n , acum):
    return n*acum

pares = list(filter(pares, numeros))
res = reduce(producto, pares, 1)
print(res)