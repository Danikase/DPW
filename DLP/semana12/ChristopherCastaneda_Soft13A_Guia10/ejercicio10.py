registro_peliculas = []

while True:
    print("\nOpciones:")
    print("1. Agregar una película")
    print("2. Eliminar una película")
    print("3. Ver todas las películas vistas")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        titulo = input("Introduce el título de la película: ")
        registro_peliculas.append(titulo)
        print(f"La película '{titulo}' ha sido agregada al registro.")
    
    elif opcion == "2":
        titulo = input("Introduce el título de la película a eliminar: ")
        if titulo in registro_peliculas:
            registro_peliculas.remove(titulo)
            print(f"La película '{titulo}' ha sido eliminada del registro.")
        else:
            print(f"La película '{titulo}' no se encuentra en el registro.")
    
    elif opcion == "3":
        print("\nPelículas vistas:")
        if not registro_peliculas:
            print("No has visto ninguna película.")
        else:
            for idx, pelicula in enumerate(registro_peliculas, start=1):
                print(f"{idx}. {pelicula}")
    
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
