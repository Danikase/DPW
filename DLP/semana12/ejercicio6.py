#  Imprimir los números de la serie de Fibonacci antes del 25

a, b = 0, 1

fib = [a, b]

while True:
    siguiente = a + b
    if siguiente >= 25:
        break
    a, b = b, siguiente
    fib[len(fib):len(fib)] = [siguiente]

print("Los números de la serie de Fibonacci menores que 25 son:")
for numero in fib:
    print(numero)
