# 8. Anagrama
# Crea un programa que verifique si dos cadenas son anagramas. Se considera que dos palabras son anagramas si tienen las mismas letras en diferente orden, por ejemplo, lácteo y coleta.
c1 = input("Palabra 1: ")
c2 = input("Palabra 2: ")
anagrama = True
if len(c1) == len(c2):
    for i in c1:
        if not i in c2:
            anagrama = False
    for i in c2:
        if not i in c1:
            anagrama = False
else:
    anagrama = False

print("Es anagrama" if anagrama else "No es anagrama")