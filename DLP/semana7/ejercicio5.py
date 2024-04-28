print("Determinacion de paridad")

num = int(input("Ingrese un numero: "))

match num:

    case num if num % 2 == 0:
        print("El número es par")
    
    case _:
        print("El numero es impar")