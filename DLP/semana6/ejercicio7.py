print("convertor de medidas")

pulgadas = float(input("Ingrese la cantidad en pulgadas: "))

centimetros = pulgadas * 2.54
metros = centimetros / 100
kilometros = centimetros / 100000

print(f"{pulgadas} pulgadas equivalen a:")
print(f"{centimetros} pulgadas")
print(f"{metros} pulgadas")
print(f"{kilometros} pulgadas")