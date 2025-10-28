# 9. Agrupación de palabras por longitud
# Dada una lista de palabras, crea un diccionario donde la clave es la longitud de la palabra y el valor es una lista de palabras de esa longitud. Usa map y filter 

palabras = ["sol", "luna", "estrella", "cielo", "mar"]
res = {}
    
def logitudes(palabra):
    return len(palabra)
    
listLen = set(map(logitudes, palabras))
for longitud in listLen:
    res[longitud] = list(filter(lambda pal: len(pal) == longitud , palabras))

print(res)

