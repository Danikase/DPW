print("Determinación del tipo de triángulo")

lado1 = int(input("Ingrese la longitud del primer lado: "))
lado2 = int(input("Ingrese la longitud del segundo lado: "))
lado3 = int(input("Ingrese la longitud del tercer lado: "))

if lado1 == lado2 == lado3:
    print("El triángulo es equilátero.")

elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles.")
    
else:
    print("El triángulo es escaleno.")