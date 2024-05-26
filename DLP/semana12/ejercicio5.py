# Calcular el factorial de un número 

numero = int(input("Ingresa un número para calcular su factorial: "))

if numero < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1
    n = numero
    while n > 1:
        factorial *= n
        n -= 1
    print("El factorial de", numero, "es", factorial)