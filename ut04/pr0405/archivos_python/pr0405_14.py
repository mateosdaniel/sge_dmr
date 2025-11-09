# 14. Aplicar operaciones de cadena
# Dada una lista de cadenas, usa map y filter para crear una nueva lista con las cadenas que tengan más de tres letras y en las que todas las letras sean mayúsculas. Además, convierte el primer carácter en minúscula.

palabras = ["HOLA", "MUNDO", "SOL", "CIELO", "mar"]

filtradas = filter(lambda x: len(x) > 3 and x.isupper(), palabras)
resultado = list(map(lambda x: x[0].lower() + x[1:], filtradas))

print(resultado)