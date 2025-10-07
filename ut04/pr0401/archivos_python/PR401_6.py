c = int(input("Introduce la cantidad: "))
i = input("Introduce la unidad de medida inicial: ").lower()
f = input("Introduce la unidad de medida final: ").lower()

#Pasa todo a metros
if(not i == "metros"):
    if(i == "milimetros"):
        c = c / 1000
    elif(i == "centimetros"):
        c = c / 100
    elif(i == "kilometros"):
        c = c * 1000
        
#Convierte a la nueva unidad
if(not f == "metros"):
    if(f == "milimetros"):
        c = c * 1000
    elif(f == "centimetros"):
        c = c * 100
    elif f == "kilometros":
        c = c / 1000
print(c)