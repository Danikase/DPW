registro = {
    "Juanito": [10, 10, 10],
    "Alcachofa": [10, 10, 10],
    "Alma": [4, 7, 7],
    "Marcela": [8, 7, 8]
}

def consultar_registro(nombre):
    if nombre in registro:
        print(registro)

def consultar_promedio(registro, nombre):
    if nombre not in registro:
        print(f"El estudiante {nombre} no se encuentra en el registro")
        return None
    
    calificaciones = registro[nombre]
    if not calificaciones:
        return None
    
    promedio = sum(calificaciones) / len(calificaciones)
    return promedio



while True:
    print("\n1. Consultar registro")
    print("2. Consultar Promedio")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        consultar_registro()
    elif opcion == "2":
        consultar_promedio()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")