# Generador de contraseñas
# Crea un programa que genere una contraseña aleatoria de una longitud que indique el usuario. La contraseña debe incluir letras mayúsculas, minúsculas, números y símbolos especiales.

from random import *

lon = int(input("Dime la longitud de la contraseña: "))
chars = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789-.,_:;!·$%&/()=@#~€¬?¿¡"
password = ""
for i in range(lon):
    password = password + chars [ randint(0, len(chars) - 1) ]

print(password)

# UTILIZANDO LA TABLA ASCII
# on = int(input("Dime la longitud de la contraseña: "))

# password = ""
# for i in range(lon):
#    password = password + chr(randint(33, 126))

# print(password)