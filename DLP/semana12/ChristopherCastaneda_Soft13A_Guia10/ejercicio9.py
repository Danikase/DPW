registro_gastos = []

while True:
    print("\nOpciones:")
    print("1. Agregar un gasto")
    print("2. Eliminar un gasto")
    print("3. Ver todos los gastos")
    print("4. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        descripcion = input("Introduce la descripción del gasto: ")
        cantidad = float(input("Introduce la cantidad del gasto: "))
        gasto = {"descripcion": descripcion, "cantidad": cantidad}
        registro_gastos.append(gasto)
        print(f"Gasto '{descripcion}' por {cantidad} agregado al registro.")
    
    elif opcion == "2":
        descripcion = input("Introduce la descripción del gasto a eliminar: ")
        encontrado = False
        for gasto in registro_gastos:
            if gasto["descripcion"].lower() == descripcion.lower():
                registro_gastos.remove(gasto)
                print(f"Gasto '{descripcion}' eliminado del registro.")
                encontrado = True
                break
        if not encontrado:
            print(f"No se encontró el gasto '{descripcion}'.")
    
    elif opcion == "3":
        print("\nRegistro de gastos:")
        if not registro_gastos:
            print("No hay gastos registrados.")
        else:
            for idx, gasto in enumerate(registro_gastos, start=1):
                print(f"{idx}. {gasto['descripcion']} - {gasto['cantidad']} unidades monetarias")
    
    elif opcion == "4":
        print("Saliendo del programa.")
        break
    
    else:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
