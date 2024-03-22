print("Calcular Area")

#Solicitar al usuario el radio del círculo y guardarlo en una variable llamada "radio"
radio = float(input("Ingrese el radio: "))

#Calcular el área de un círculo utilizando la fórmula A=πr² donde para elevar el radio a la potencia 2 usaremos el pow() 
a = (3.1416) * pow(radio,2)

#Esto nos mostrara el resultado
print("tu respuesta es: " + str(a))