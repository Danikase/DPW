print("Determinación de la estación del año")

print("1-enero",   "5-mayo",   "9-septiembre")
print("2-febrero", "6-junio",  "10-octubre")
print("3-marzo",   "7-julio",  "11-noviembre")
print("4-abril",   "8-agosto", "12-diciembre")

mes = int(input("Ingrese un numero del 1-12 que corresponde a cada mes: "))

match mes:

    case mes if mes in [12,1,2]:
        print("La estacion es invierno")

    case mes if mes in [3, 4, 5]:
        print("La estación es primavera.")

    case mes if mes in [6, 7, 8]:
        print("La estación es verano.")

    case mes if mes in [9, 10, 11]:
        print("La estación es otoño.")

    case _:
        print("Número de mes inválido. Debe ser un número del 1 al 12.")
         