print("Tiempo de lectura")

numero_paginas = int(input("Ingrese el número de páginas del libro: "))
velocidad_lectura = int(input("Ingrese su velocidad de lectura en páginas por hora: "))
    
tiempo_lectura = numero_paginas / velocidad_lectura
    
print("El tiempo necesario para leer el libro es de aproximadamente", tiempo_lectura, "horas.")