def calcular_tiempo_coccion(peso):
    tiempo_coccion = 45  # Tiempo de cocción inicial para el primer kilogramo
    
    if peso > 1:
        tiempo_coccion += (peso - 1) * 30  # Añadir 30 minutos por cada kilogramo extra
    
    return tiempo_coccion

try:
    peso_pollo = float(input("Ingrese el peso del pollo en kilogramos: "))
    
    if peso_pollo <= 0:
        print("El peso del pollo debe ser un valor positivo mayor que cero.")
    else:
        tiempo_total = calcular_tiempo_coccion(peso_pollo)
        print(f"El tiempo de cocción para un pollo de {peso_pollo} kg es de {tiempo_total} minutos.")
        
except ValueError:
    print("Por favor, ingrese un valor numérico para el peso del pollo.")
