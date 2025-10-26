# 7. Rotar caracteres de una cadena
# Escribe una función que rote una cadena hacia la izquierda un número dado de veces.
text = input("Escribe una cadena a continuación: ")
n = 2
rotada = text[n:] + text[:n]
print(rotada)
