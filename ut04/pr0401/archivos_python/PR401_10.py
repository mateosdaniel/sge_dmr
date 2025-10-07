n = input("Introduce un número: ")
while(not n.isdigit()):
    n = input("Ese no es un número válido, introduce un número válido: ")
n = int(n)

if n <= 1:
    es_primo = False
else:
    es_primo = True
    # Bucle desde 2 hasta la raiz cuadrada del número más uno porque el segundo parametro no está incluido.
    # Solo compruebo hasta la raiz cuadrada porque uno de los divisores siempre está en el rango menor o igual al número.
    for i in range(2, int(n**0.5) + 1):
        # Si es divisible, no es primo
        if n % i == 0:
            es_primo = False
            break

if es_primo:
    print(f"El número {n} es primo.")
else:
    print(f"El número {n} no es primo.")
