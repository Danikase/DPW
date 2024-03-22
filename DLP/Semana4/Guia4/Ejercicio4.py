print("calculadora del volumen de un cubo")

# Con esta variable obtendremos del usuario los datos que necesitamos para calcular el volume del cubo.
l = float(input("ingrese el valor del lado del cubo: "))

# La formula a utilizar es sencilla solo se eleva a la potencia 3 la variable l con pow()
v = pow(l,3)

# Con esto mostraremos el resultado final
print ("el volume del cubo es " + str(v))
