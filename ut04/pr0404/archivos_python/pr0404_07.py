# 7. Filtrar claves y valores

dic = {
    "empleado1" : 1000,
    "empleado2" : 900,
    "empleado3" : 800,
    "empleado4" : 1200
}
umbral = 900
resultado = {nombre:salario for nombre,salario in dic.items() if salario > umbral}
print(resultado)