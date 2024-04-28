print("Determinacion del dia de la semana")

print("Suponiendo que cada numero es igual a cada de dia de la semana ejemplo: 1 es lunes")
day = int(input("Elija un numero del 1 al 7 que corresponde a cada dia de la semana: "))

match day:

    case day if day == 1:
        print("El dia seleccionado es Lunes")

    case day if day == 2:
        print("El dia seleccionado es Martes")

    case day if day == 3:
        print("El dia seleccionado es Miercoles")

    case day if day == 4:
        print("El dia seleccionado es Jueves")

    case day if day == 5:
        print("El dia seleccionado es Viernes")

    case day if day == 6:
        print("El dia seleccionado es Sabado")

    case day if day == 7:
        print("El dia seleccionado es Domingo")

    case _:
        print("El numero ingresado no es valido")