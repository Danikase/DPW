print()

x = int(input("Introduce la coordenada x del punto: "))
y = int(input("Introduce la coordenada y del punto: "))


if x > 0:
    if y > 0:
        print("El punto está en el primer cuadrante.")
    else:
        print("El punto está en el cuarto cuadrante.")

elif x < 0:
    if y > 0:
        print("El punto está en el segundo cuadrante.")
    else:
        print("El punto está en el tercer cuadrante.")

else:
    if y != 0:
        print("El punto está sobre el eje y.")
    else:
        print("El punto está en el origen.")