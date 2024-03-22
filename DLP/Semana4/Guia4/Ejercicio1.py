print("Calcula volumen de una esfera")

#Pedir al usuario que ingrese los datos solicitados a traves de la variable "radio"
#En este caso uso float para que el usuario tenga más libertad con los datos que desee ingresar
radio = float(input("Escribe el radio: "))

#Formula para calcular el volume de una esfera: (4/3)*3.1416*r^3 donde usaremos pow() para poder elevar a la potencia 3
Vol = (4/3) * (3.1416) * pow(radio,3)

#Imprimiremos aca el resultado
print("es igual a " + str(Vol))