print("Determinacion del tipo de numero ")

num = int(input("Ingrese un numero puede ser positivo o negativo: "))

match num:

    case num if num > 0:
        print("Su numero es postivo")

    case num if num < 0:
        print("Su numero es negativo")

    case _:
        print("Su numero es igual a cero")