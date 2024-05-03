print()

fib = [0, 1]

for i in range(2, 10):
    siguiente = fib[-1] + fib[-2]
    fib.append(siguiente)

print("Los primeros 10 números de la serie de Fibonacci son:")
for numero in fib:
    print(numero)
