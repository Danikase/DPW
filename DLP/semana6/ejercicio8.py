dia = int(input("Ingrese el día: "))
mes = int(input("Ingrese el mes: "))
año = int(input("Ingrese el año: "))

fecha_valida = True

if mes < 1 or mes > 12:
    fecha_valida = False
elif mes in (1, 3, 5, 7, 8, 10, 12):
    if dia < 1 or dia > 31:
        fecha_valida = False
elif mes in (4, 6, 9, 11):
    if dia < 1 or dia > 30:
        fecha_valida = False
elif mes == 2:
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        if dia < 1 or dia > 29:
            fecha_valida = False
    elif dia < 1 or dia > 28:
        fecha_valida = False


if fecha_valida:
    print("La fecha ingresada es válida.")
else:
    print("La fecha ingresada no es válida.")