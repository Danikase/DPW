registro_ejercicios = []

while True:
    print("\nOpciones:")
    print("1. Agregar un ejercicio")
    print("2. Eliminar un ejercicio")
    print("3. Ver todos los ejercicios realizados")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Introduce el nombre del ejercicio: ")
        duracion = input("Introduce la duración del ejercicio (en minutos): ")
        ejercicio = {"nombre": nombre, "duracion": duracion}
        registro_ejercicios.append(ejercicio)
        print(f"El ejercicio '{nombre}' con duración de {duracion} minutos ha sido agregado al registro.")
    
    elif opcion == "2":
        nombre = input("Introduce el nombre del ejercicio a eliminar: ")
        encontrado = False
        for ejercicio in registro_ejercicios:
            if ejercicio["nombre"].lower() == nombre.lower():
                registro_ejercicios.remove(ejercicio)
                print(f"El ejercicio '{nombre}' ha sido eliminado del registro.")
                encontrado = True
                break
        if not encontrado:
            print(f"El ejercicio '{nombre}' no se encuentra en el registro.")
    
    elif opcion == "3":
        print("\nEjercicios realizados:")
        if not registro_ejercicios:
            print("No has realizado ningún ejercicio.")
        else:
            for idx, ejercicio in enumerate(registro_ejercicios, start=1):
                print(f"{idx}. Nombre: {ejercicio['nombre']}, Duración: {ejercicio['duracion']} minutos")
    
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
