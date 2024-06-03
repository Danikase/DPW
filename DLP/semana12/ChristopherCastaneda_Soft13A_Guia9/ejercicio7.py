altura = 5
i = 0

while i < altura:
    # Imprimir espacios
    j = 0
    while j < altura - i - 1:
        print(" ", end="")
        j += 1

    # Imprimir asteriscos
    k = 0
    while k < 2 * i + 1:
        print("*", end="")
        k += 1

    # Pasar a la siguiente línea
    print()
    i += 1
