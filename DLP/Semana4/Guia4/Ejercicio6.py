print("Calculadora de velocidad")

# Primero se pide al usuario la distancia recorrida y el tiempo transcurrido
dist = float(input("Ingrese la distancia en km que ha recorrido (kilometros): "))
tiempo = float(input("Ingrese el tiempo transcurrido (en horas): "))

# Se calcula la velocidad promedio dividiendo la distancia y tiempo
velocidad = dist/tiempo  

# Mostramos el resultado final a los usuarios
print("la velocidad promedio es: ", velocidad, "km/h")
