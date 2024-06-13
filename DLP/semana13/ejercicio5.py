def generar_pares(n):
    return [i for i in range(0, n+1) if i % 2 == 0]

# Ejemplo de uso:
print(generar_pares(10))  # Salida: [0, 2, 4, 6, 8, 10]
