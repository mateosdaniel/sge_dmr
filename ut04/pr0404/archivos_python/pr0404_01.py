# Buscar valor en un diccionario

text = input("Ingresa el nombre de una fruta: ")
comercio = {
    "naranjas":"10€",
    "peras":"20€",
    "fresas":"30€",
}

if text in comercio.keys():
    print(comercio.get(text))
else:
    print("La fruta no se encuentra en stock.")