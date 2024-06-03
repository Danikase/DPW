tareas = []

while True:
    print("\nOpciones:")
    print("1. Agregar una tarea")
    print("2. Marcar una tarea como completada")
    print("3. Ver todas las tareas")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        tarea = input("Introduce la descripción de la tarea: ")
        tareas.append({"descripcion": tarea, "completada": False})
        print(f"Tarea '{tarea}' agregada.")
    
    elif opcion == "2":
        tarea_a_completar = input("Introduce la descripción de la tarea a marcar como completada: ")
        encontrada = False
        for tarea in tareas:
            if tarea["descripcion"].lower() == tarea_a_completar.lower() and not tarea["completada"]:
                tarea["completada"] = True
                print(f"Tarea '{tarea_a_completar}' marcada como completada.")
                encontrada = True
                break
        if not encontrada:
            print(f"No se encontró la tarea '{tarea_a_completar}' o ya está completada.")
    
    elif opcion == "3":
        print("\nLista de tareas:")
        if not tareas:
            print("No hay tareas.")
        else:
            for idx, tarea in enumerate(tareas, start=1):
                estado = "Completada" if tarea["completada"] else "Pendiente"
                print(f"{idx}. {tarea['descripcion']} - {estado}")
    
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
