# 11. Transformar a camelCase
# Escribe un programa que transforme una cadena de palabras separadas por espacios o guiones en formato camelCase
# (la primera letra de cada palabra, excepto la primera, debe ser mayúscula y no debe haber espacios ni guiones).

texto = input("Escribe una cadena: ").title().replace(" ", "").replace("-","")
texto = texto[0].lower() + texto[1:]

print(texto)