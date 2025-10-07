n = int(input("Indica cuantos números de la secuencia de Fibonacci quieres: "))

if(n == 1):
    print("1")
elif(n == 2):
    print("1, 1" )
else:
    fib1 = 1
    fib2 = 1
    final = "1, 1"
    for i in range(n - 2):
        t = fib1
        fib1 = fib2
        fib2 += t
        final += ", " + str(fib2) 
    print(final)