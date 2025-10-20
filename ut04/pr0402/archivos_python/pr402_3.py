# 3. Verificar palíndromo
# Escribe un programa que verifique si una cadena es un palíndromo (se lee igual de izquierda a derecha y de derecha a izquierda).
text = input("Escribe una cadena y te diré si es un palíndromo: ").lower().replace(" ", "")
if text == text[::-1]:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")
