lista_reproduccion = []

while True:
    print("\nOpciones:")
    print("1. Agregar una canción")
    print("2. Eliminar una canción")
    print("3. Ver la lista de reproducción")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        cancion = input("Introduce el nombre de la canción a agregar: ")
        lista_reproduccion.append(cancion)
        print(f"La canción '{cancion}' ha sido agregada a la lista de reproducción.")
    
    elif opcion == "2":
        cancion = input("Introduce el nombre de la canción a eliminar: ")
        if cancion in lista_reproduccion:
            lista_reproduccion.remove(cancion)
            print(f"La canción '{cancion}' ha sido eliminada de la lista de reproducción.")
        else:
            print(f"La canción '{cancion}' no se encuentra en la lista de reproducción.")
    
    elif opcion == "3":
        print("\nLista de reproducción:")
        if not lista_reproduccion:
            print("La lista de reproducción está vacía.")
        else:
            for idx, cancion in enumerate(lista_reproduccion, start=1):
                print(f"{idx}. {cancion}")
    
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
