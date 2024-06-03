registro_libros = []

while True:
    print("\nOpciones:")
    print("1. Agregar un libro")
    print("2. Eliminar un libro")
    print("3. Ver todos los libros leídos")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        libro = input("Introduce el título del libro a agregar: ")
        registro_libros.append(libro)
        print(f"El libro '{libro}' ha sido agregado al registro.")
    
    elif opcion == "2":
        libro = input("Introduce el título del libro a eliminar: ")
        if libro in registro_libros:
            registro_libros.remove(libro)
            print(f"El libro '{libro}' ha sido eliminado del registro.")
        else:
            print(f"El libro '{libro}' no se encuentra en el registro.")
    
    elif opcion == "3":
        print("\nLibros leídos:")
        if not registro_libros:
            print("No has leído ningún libro.")
        else:
            for idx, libro in enumerate(registro_libros, start=1):
                print(f"{idx}. {libro}")
    
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
