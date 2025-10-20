# 3. Contador de frecuencias de palabra

text = input("Escribe una frase: ")

palabras = text.split()
ocurrencias = {}

for palabra in palabras:
     ocurrencias[palabra] = ocurrencias.get(palabra, 0) + 1
     
print(ocurrencias)