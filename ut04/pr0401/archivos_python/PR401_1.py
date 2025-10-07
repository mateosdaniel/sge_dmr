numero = input("Introduce un número positivo: ")
while (not numero.isdigit()):
    numero = input("Ese no es un número válido, introduce un número válido: ")
print("correcto")

# MEJORADO
# while( not input("Introduce un número positivo: ").isdigit() ):
#   pass
# print("correcto")