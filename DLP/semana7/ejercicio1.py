print("calculadora de operaciones basicas")

num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un numero: "))

print("elija una opcion y luego escribala")
print("suma")
print("resta")
print("multiplicacion")
print("division")

operacion = input("elija una operacion: ")

match operacion:

    case "suma":
       print(num1 + num2)

    case "resta":
        print(num1 - num2)
        
    case "multiplicacion":
        print(num1 * num2)

    case "division":
        print(num1 / num2)