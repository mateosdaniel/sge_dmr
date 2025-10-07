# 12. Codificación RLE (Run-Length Enconding)
# Escribe una función que implemente la codificación por longitud de ejecución (RLE), que consiste en comprimir una cadena representando las secuencias
# consecutivas de caracteres iguales con el carácter seguido de la cantidad de repeticiones.
cadena = input("Escribe una cadena para comprimir: ")

count = 0
prev = ""
res = ""

for c in cadena:
    if prev == c:
        count += 1
    else:
        if prev:
            res = res + prev
            res = res + str(count)
        prev = c
        count = 1
res = res + prev
res = res + str(count)
print(res)