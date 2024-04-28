print("Determinación del tipo de triángulo")

lado1 = int(input("Ingrese la longitud del primer lado: "))
lado2 = int(input("Ingrese la longitud del segundo lado: "))
lado3 = int(input("Ingrese la longitud del tercer lado: "))

match (lado1, lado2, lado3):
    case (l1, l2, l3) if l1 == l2 == l3:
        print("El triángulo es equilátero.")

    case (l1, l2, l3) if l1 == l2 or l1 == l3 or l2 == l3:
        print("El triángulo es isósceles.")

    case _:
        print("El triángulo es escaleno.")
    