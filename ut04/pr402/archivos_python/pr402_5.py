# 5. Eliminar caracteres repetidos
# Escribe una función que elimine los caracteres duplicados en una cadena, manteniendo solo la primera aparición de cada uno.
text = input("Escribe una cadena a continuación: ")
new_text = ""
for i in range (len(text)):
    if not text[i] in new_text:
        new_text = new_text + text[i]
print(new_text)