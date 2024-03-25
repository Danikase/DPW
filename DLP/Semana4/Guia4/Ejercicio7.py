print("tiempo de cocción")

peso = float(input("Ingrese el peso del pollo en kilogramos: "))
tiempo_coccion = 45 + (max(peso - 1, 0) * 30)
print("El tiempo de cocción necesario es de aproximadamente", tiempo_coccion, "minutos.")