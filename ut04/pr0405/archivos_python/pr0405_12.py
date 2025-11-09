# 12. Calcular producto cartesiano
# Dadas dos listas de números, usa map para obtener el producto cartesiano de ambas listas, devolviendo una lista de tuplas.
import itertools

lista1 = [1, 2]
lista2 = [3, 4]

resultado = list(itertools.product(lista1, lista2))
print(resultado)