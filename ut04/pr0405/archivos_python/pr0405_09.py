# Agrupación de palabras por longitud
# Dada una lista de palabras, crea un diccionario donde la clave es la longitud de la palabra y el valor es una lista de palabras de esa longitud. Usa map y filter 

palabras = ["sol", "luna", "estrella", "cielo", "mar"]
lista = []
res = {}

def longitud(i):
    for palabra in palabras:
        res[len(palabra)] = any
    return i 
    
def palabra(palabra):
    return palabra in res


res[list((map(longitud, palabras)))] = list(filter(palabra, palabras))
print (res)

