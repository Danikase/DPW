print("Determinar Cuadrante")

x = float(input("Introduce la coordenada x del punto: "))
y = float(input("Introduce la coordenada y del punto: "))

match (x, y):
    case (0, 0):
        print("El punto está en el origen.")
    case (x, 0) if x != 0:
        print("El punto está sobre el eje y.")
    case (0, y) if y != 0:
        print("El punto está sobre el eje x.")
    case (x, y) if x > 0 and y > 0:
        print("El punto está en el primer cuadrante.")
    case (x, y) if x < 0 and y > 0:
        print("El punto está en el segundo cuadrante.")
    case (x, y) if x < 0 and y < 0:
        print("El punto está en el tercer cuadrante.")
    case (x, y) if x > 0 and y < 0:
        print("El punto está en el cuarto cuadrante.")
    case _:
        print("El punto está en un caso especial.")
