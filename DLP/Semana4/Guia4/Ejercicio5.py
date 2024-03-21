print("Calculadora de la hipotenusa de un triángulo rectángulo")

# import math se usa para hacer uso de funciones matemáticas como 'sqrt' 
import math

# Estas seran las dos variables que usaremos para recolectar los datos del usuario
cateto1  = float(input("Ingrese el valor del primer cateto: "))
cateto2  = float(input("Ingrese el valor del segundo cateto: "))

# La función math.sqrt() nos permite utilizar raíz cuadrada, la cual utilizamos para el calculo de la hipotenusa
# Otra manera en la que se pudo haber hecho este ejercicio es en lugar de usar 'pow()' solo se puede usar doble asterisco
# hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
hipotenusa = math.sqrt(pow(cateto1,2)+pow(cateto2,2))
 
# Mostramos el resultado al usuario 
# Para mostrar el resultado esta vez no fue necesario convertir la variable en 'str()' porque python lo hizo automaticamente
print ("La longitud de la hipotenusa es: ", hipotenusa)