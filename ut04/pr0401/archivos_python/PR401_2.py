n = int(input("Introduce un número : "))
k = int(input("Introduce cuantas veces quieres que se multiplique : "))
a = 0
while(a <= k):
    print(str(n) + " * " + str(a) + " = " + str(n*a))
    a=a+1

# MEJORADO
# n = int(input("Introduce un número : "))
# k = int(input("Introduce cuantas veces quieres que se multiplique : "))
# for iter in range(1, k+1):
#     print( f"{n} * {iter} = { n*iter }" )