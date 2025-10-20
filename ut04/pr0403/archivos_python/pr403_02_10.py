# 10. Lista de listas: 
# Crea una lista de listas que represente una matriz de números y escribe una función que devuelva la suma de cada fila y columna.

lista = [
    [1,2,3,4],
    [9,5,2,5],
    [6,2,5,5]
]

suma_filas = []

for fila in lista:
    suma = 0
    for num in fila:
        suma += num
    suma_filas.append(suma)

suma_columnas = [0] * len(lista[0])
for fila in lista:
    for i in range(len(fila)):
        suma_columnas[i] += fila[i]

print(suma_filas)
print(suma_columnas)