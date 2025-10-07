lista = []
print("A continuación se le pedirá que introduzca un total de 5 números para identificar cual es el mayor y el menor de los 5")
for i in range(5):
    n = input("Introduce un número entero positivo : ")
    while(not n.isdigit()):
        n = input("Introduce un número válido por favor: ")
    lista.append(int(n))
print("El número mas grande es " + str(max(lista)) + " y el más pequeño es " + str(min(lista)))

