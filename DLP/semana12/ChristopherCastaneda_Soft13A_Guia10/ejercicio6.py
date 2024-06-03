plan_viaje = []

while True:
    print("\nOpciones:")
    print("1. Agregar un lugar")
    print("2. Eliminar un lugar")
    print("3. Ver todos los lugares que planea visitar")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        lugar = input("Introduce el nombre del lugar a agregar: ")
        plan_viaje.append(lugar)
        print(f"El lugar '{lugar}' ha sido agregado al plan de viaje.")
    
    elif opcion == "2":
        lugar = input("Introduce el nombre del lugar a eliminar: ")
        if lugar in plan_viaje:
            plan_viaje.remove(lugar)
            print(f"El lugar '{lugar}' ha sido eliminado del plan de viaje.")
        else:
            print(f"El lugar '{lugar}' no se encuentra en el plan de viaje.")
    
    elif opcion == "3":
        print("\nLugares que planea visitar:")
        if not plan_viaje:
            print("No ha agregado ningún lugar a su plan de viaje.")
        else:
            for idx, lugar in enumerate(plan_viaje, start=1):
                print(f"{idx}. {lugar}")
    
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
