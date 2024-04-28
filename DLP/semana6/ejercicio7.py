print("Determinación de la estación del año")

mes = int(input("Ingrese un numero del 1-12 que corresponde a cada mes: "))

if mes in [12,1,2]:
    print("La estacion es invierno")

elif mes in [3, 4, 5]:
    print("La estación es primavera.")

elif mes in [6, 7, 8]:
    print("La estación es verano.")

elif mes in [9, 10, 11]:
    print("La estación es otoño.")

else:
    print("Número de mes inválido. Debe ser un número del 1 al 12.")