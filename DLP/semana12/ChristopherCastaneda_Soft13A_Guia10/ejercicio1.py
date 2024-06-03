lista_compra = []

while True:
    print("\nOpciones:")
    print("1. Agregar un artículo a la lista")
    print("2. Eliminar un artículo de la lista")
    print("3. Ver la lista de la compra")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        articulo = input("Introduce el nombre del artículo a agregar: ")
        lista_compra.append(articulo)
        print(f"{articulo} ha sido agregado a la lista.")
    
    elif opcion == "2":
        articulo = input("Introduce el nombre del artículo a eliminar: ")
        if articulo in lista_compra:
            lista_compra.remove(articulo)
            print(f"{articulo} ha sido eliminado de la lista.")
        else:
            print(f"{articulo} no se encuentra en la lista.")
    
    elif opcion == "3":
        print("\nLista de la compra:")
        for idx, articulo in enumerate(lista_compra, start=1):
            print(f"{idx}. {articulo}")
        if not lista_compra:
            print("La lista está vacía.")
    
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
