# Imprimir la tabla de multiplicar que el usuario desee usando While

num = int(input("Escriba la tabla de multiplicar que desee saber: "))
mult = 0

while mult in range(0, 10):
    mult += 1
    print(num, "X", mult, "=", num*mult)
    