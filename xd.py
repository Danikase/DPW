list = []

def promedy():
    cantidad = int(input('Ingrese la cantidad de numeros a promediar: '))
    n = 0 

    while n < cantidad:
        num = int(input("Ingresar el numero: "))
        list.append(num)
        prom = sum(list) / cantidad
        n = n+1

    print(list)
    print(sum(list))
    print(prom)

promedy()