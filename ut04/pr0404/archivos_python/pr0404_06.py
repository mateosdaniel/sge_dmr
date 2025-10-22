# 6. Combinar dos diccionarios

dic = {
    "ordenador" : 1000,
    "ratón" : 30,
    "cascos" : 50
}
dic2 = {
    "ordenador" : 800,
    "teclado" : 40,
    "ratón" : 25
}
dic_comun = dic
for i in dic2:
    if i in dic_comun:
        dic_comun[i] = dic.get(i) + dic2.get(i)
    else:
        dic_comun[i] = dic2.get(i)
print(dic_comun)