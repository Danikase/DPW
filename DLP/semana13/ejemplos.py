# Ejemplo1 
# Definir una funcion
def avg(valor1, valor2):
    return (valor1 + valor2) / 2

# Ejecutar funcion
print("EL promedio de: ", avg(8.5, 7.2))


# Ejemplo2
def say_hello():
    print('hello')


# Ejemplo3
def say_hello():
    print('hello')

#Llamada a la funcion (primer nivel de indentacion)
say_hello()


# Ejemplo4
# Retonarnar un valor
def one():
    return 1

print("Valor de funcion One: ", one())


# Ejemplo 5
# Agregar mas expresiones
def one():
    return 1

print("Valor de funcion One: ", one())

if one() == 1:
    print("Funciona")

else:
    print("Algo esta roto")


# Ejemplo6
def vacia():
    x = 0
    #return none

print(vacia())


# Ejemplo7
# Funcion que retorna muliples valores
def multiple():
    return 0, 1 # Retorna una tupla con dos valores

result = multiple()

print(result)   # Output: (0, 1)
print(type(result)) # Output: <class 'tuple'>