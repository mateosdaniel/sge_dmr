from random import *
r = randint(0, 100)
acertado = False
while(acertado == False):
    n = int(input("Introduce un número del 0 al 100: "))
    if(n > r):
        print("El número es más bajo")
    elif(n < r):
        print("El número es más alto")
    else: 
        acertado = True
        print ("Acertaste!")
    