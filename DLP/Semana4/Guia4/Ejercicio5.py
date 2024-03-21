print("Calculadora de la hipotenusa de un triángulo rectángulo")

# import math se usa para hacer uso de funciones matemáticas como sqrt 
import math

# Estas seran las dos variables que usaremos para recolectar los datos del usuario
cateto1  = float(input("Ingrese el valor del primer cateto: "))
cateto2  = float(input("Ingrese el valor del segundo cateto: "))

hipotenusa = math.sqrt(pow(cateto1,2)+pow(cateto2,2))
#math.sqrt(pow(cateto1,2)pow(cateto2,2))
#math.sqrt((cateto1**2)+(cateto2**2))   

print ("La longitud de la hipotenusa es: ", hipotenusa)