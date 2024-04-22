print("aumento del sueldo")

sueldo = float(input("Ingrese su salario: $"))

if sueldo < 1000:
    aumento = sueldo * 0.15
    nuevo_sueldo = sueldo + aumento
    print("Su salario anterior era:", sueldo)
    print("Se le aplicó un aumento del 15%.")
    print(nuevo_sueldo)

else:
    aumento = sueldo * 0.12
    nuevo_sueldo = sueldo + aumento
    print("Su salario anterior era:", sueldo)
    print("Se le aplicó un aumento del 12%.")
    print(nuevo_sueldo)