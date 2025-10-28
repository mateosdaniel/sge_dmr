# 6. Combinar operaciones en listas anidadas
# Dada una lista de listas de enteros, usa map, filter, y reduce para obtener la suma de todos los números positivos.

from functools import reduce

numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]

# Unir las listas
def unir_listas(acum, item):
     return acum + item

lista = reduce(unir_listas, numeros, []) # unir_lista lambda --> lambda acum, item: acum + item
 
# Lista de positivos
def pos(n): 
    return n > 0

positivos = list(filter(pos, lista)) # pos lambda --> lambda n: n > 0

#Suma de los numeros positivos
def sumar(n , acum):
    return n + acum

res = reduce(sumar, positivos, 0) # sumar lambda --> lambda n, acum: n + acum
print(res)