print("Celsius a Fahrenheit")

# El usario ingresara aca los datos de los grados Celsius que desea convertir a Fahrenheit.
c = float(input("Ingrese la temperatura en Celsius: "))

# Formula para convertir de Celsius a Fahrenheit es: F= c * 9/5 +32
# En este caso utilice 9/5 para multiplicarlo con la variable "c" pero tambien es valido usar 1.8
f = c * 9/5 + 32

# Esto es lo que se utilizara para mostrar el resultado
print("la temperatura en fahrenheit es: " + str(f))