# 5. Diccionario invertido

dic = {
    "clave1" : "valor1",
    "clave2" : "valor2",
    "clave3" : "valor3",
    "clave4" : "valor4"
}

invertido = {v:k for k,v in dic.items()}
print(invertido)