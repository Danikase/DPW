agenda_contactos = []

while True:
    print("\nOpciones:")
    print("1. Agregar un contacto")
    print("2. Buscar un contacto")
    print("3. Ver todos los contactos")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Introduce el nombre del contacto: ")
        telefono = input("Introduce el número de teléfono del contacto: ")
        contacto = {"nombre": nombre, "telefono": telefono}
        agenda_contactos.append(contacto)
        print(f"Contacto {nombre} agregado con éxito.")
    
    elif opcion == "2":
        nombre_buscar = input("Introduce el nombre del contacto a buscar: ")
        encontrado = False
        for contacto in agenda_contactos:
            if contacto["nombre"].lower() == nombre_buscar.lower():
                print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
                encontrado = True
                break
        if not encontrado:
            print("Contacto no encontrado.")
    
    elif opcion == "3":
        print("\nLista de contactos:")
        if not agenda_contactos:
            print("La agenda está vacía.")
        else:
            for idx, contacto in enumerate(agenda_contactos, start=1):
                print(f"{idx}. Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}")
    
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
