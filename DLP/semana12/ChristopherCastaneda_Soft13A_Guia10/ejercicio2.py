calificaciones = []

# Ingresar 5 calificaciones
print("Introduce las calificaciones del estudiante (5 calificaciones):")
while len(calificaciones) < 5:
    calificacion = float(input(f"Introduce la calificación {len(calificaciones) + 1}: "))
    calificaciones.append(calificacion)

# Mostrar las calificaciones y calcular el promedio
while True:
    print("\nOpciones:")
    print("1. Ver las calificaciones")
    print("2. Calcular el promedio")
    print("3. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        print("\nCalificaciones del estudiante:")
        for idx, calificacion in enumerate(calificaciones, start=1):
            print(f"{idx}. {calificacion}")
    
    elif opcion == "2":
        promedio = sum(calificaciones) / len(calificaciones)
        print(f"\nEl promedio de las calificaciones es: {promedio:.2f}")
    
    elif opcion == "3":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 3.")
