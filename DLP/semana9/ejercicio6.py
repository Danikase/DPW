print("Calcular el factorial de un número")

numero = int(input("Introduce un número para calcular su factorial: "))
factorial = 1

if numero < 0:
    print("No se puede calcular el factorial de números negativos.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, numero + 1):
        factorial *= i
    print("El factorial de", numero, "es:", factorial)
