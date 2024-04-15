print("Uso de booleanos y operadores lógicos")

value1 = input("Ingrese un valor booleano true o false: ") == bool
value2 = input("Ingrese un segundo valor booleano true o false: ") == bool

Conjuncion = value1 and value2
Disyuncion = value1 or value2
Negacion1 = not value1
Negacion2 = not value2

print("conjuncion: ", Conjuncion)
print("disyuncion: ", Disyuncion)
print("Negacion del primer valor: ", Negacion1)
print("Negacion del segundo valor: ", Negacion2)