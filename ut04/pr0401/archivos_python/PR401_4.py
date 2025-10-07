n = int(input("Introduce un número impar: "))
f = "*"
while(n % 2 == 0):
    n = int(input("Introduce un número impar: "))
for a in range(0, n, 2):
    print(f.center(40))
    f += "**"   
    