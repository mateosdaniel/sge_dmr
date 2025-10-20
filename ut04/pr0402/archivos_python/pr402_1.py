# 1. Contar vocales y consonantes
# Escribe una función que reciba una cadena y cuente cuántas vocales y consonantes contiene.
text = input("Escribe una cadena y te diré cuantas vocales y consonantes tiene: ").lower()
cadena = list(text)
v = ["a", "e", "i", "o", "u"]
vocales = 0
consonantes = 0
for letra in cadena:
    if(letra) in v:
        vocales = vocales + 1
    else:
        consonantes = consonantes + 1
print(vocales)
print(consonantes)