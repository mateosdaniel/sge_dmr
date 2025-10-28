# 2. Mapeo de temperaturas
# Dada una lista de temperaturas en Celsius, usa map para convertirlas a Fahrenheit.

celsius = [0, 20, 37, 100]
res = []

def pasar_a_fah(temperatura):
    return (temperatura * 9/5) + 32

res = list(map(pasar_a_fah, celsius))
print (res)