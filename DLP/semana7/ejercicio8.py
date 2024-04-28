print("Determinacion de figuras geometricas")

lados = int(input("Ingrese el numero de lados de la figuera que desea saber: "))

match lados:

    case lados if lados == 3:
        print("Su figura puede ser un triangulo")

    case lados if lados == 4:
        print("Su figura puede ser un cuadrado o un rectangulo")

    case lados if lados == 5:
        print("Su figura es un pentagono")

    case lados if lados == 6:
        print("Su figura es un Hexagono")

    case lados if lados == 8:
        print("Su figura es un octagono")