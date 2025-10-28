#  8. Intersección de conjuntos
# Dadas dos listas de números, usa filter para obtener una lista de los elementos que están en ambas listas (sin usar conjuntos)

lista1 = [1, 2, 3, 4, 5]
lista2 = [3, 4, 5, 6, 7]
res = []
def en_ambas_listas(numero):
    return numero in lista2

res = list(filter(en_ambas_listas, lista1))
print (res)