# 1. Filtrado de una lista de números.
# Usa filter para obtener solo los números pares de una lista de entero.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res = []
x = 0

def pares(numero):
    return numero%2 == 0

res = list(filter(pares, numeros))
print (res)