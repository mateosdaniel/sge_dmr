# 10. Quitar caracteres alfanuméricos
# Escribe un programa que elimine todos los caracteres no alfanuméricos (como signos de puntuación) de una cadena.

texto = input("Escribe una cadena: ")

res = ""
for c in texto:
    if c.isalnum():
        res += c

print(res)