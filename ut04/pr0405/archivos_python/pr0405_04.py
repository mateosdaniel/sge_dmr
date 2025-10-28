# 4. Palabras con cierta longitud
# Dada una lista de palabras, usa filter para encontrar las que tienen más de cinco letras y luego map para convertirlas en mayúsculas

palabras = ["perro", "gato", "elefante", "oso", "jirafa"]
res = []
res_upper = []
def mas_de_cinco_letras(palabra):
    return len(palabra) > 5

res = list(filter(mas_de_cinco_letras, palabras))

def to_upper(palabra):
    return palabra.upper()

res_upper = list(map(to_upper, res))
print(res_upper)
