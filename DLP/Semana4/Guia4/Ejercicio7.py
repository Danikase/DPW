print("tiempo de cocción")

# 
tiempo_de_coccion = 45
peso = float(input("peso del pollo en kg: "))

if peso <= 0:
    print("El peso del pollo debe ser mayor a cero")
else:
    if peso == 1 == tiempo_de_coccion:
        print(f"El tiempo de cocción es de {tiempo_de_coccion}")