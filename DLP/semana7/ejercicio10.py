print("Determinacion de vehiculo")

ruedas = int(input("Ingrese el numero de ruedas del vehiculo que desea saber: "))

match ruedas:

    case ruedas if ruedas == 2:
        print("Su vehiculo es una motocicleta")

    case ruedas if ruedas == 4:
        print("Su vehiculo es un carro")

    case ruedas if ruedas > 4:
        print("Su vehiculo es un camion")