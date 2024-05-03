print("Piramide de asteriscos")

altura = 5  

for i in range(altura):  

    for j in range(altura - i - 1):
        print(" ", end="")

    for k in range(2 * i + 1):
        print("*", end="")
    print()
