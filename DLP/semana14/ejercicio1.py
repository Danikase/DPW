import os

file = './DLP/semana14/Tabladel1.txt'
#file = './DLP/semana14'

def search_multiply(n, m):
    if n < 1 or n > 10  or m < 1 or m > 10:
        print("Los numeros deben de estar entre 1 y 10")
        return
    
    search_number = n
        
    with open(file, "r") as f:
        for line in f:
            if search_number in line:
                print(line)

    
    
n = int(input("Ingrese un numero del 1 al 10: "))