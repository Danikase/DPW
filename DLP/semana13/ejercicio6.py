def calculadora(a, b, operacion):
    if operacion == 'suma':
        return a + b
    elif operacion == 'resta':
        return a - b
    elif operacion == 'multiplicacion':
        return a * b
    elif operacion == 'division':
        if b != 0:
            return a / b
        else:
            return "Error: División por cero"
    else:
        return "Operación no válida"

# Ejemplo de uso:
print(calculadora(10, 5, 'suma'))         # Salida: 15
print(calculadora(10, 5, 'resta'))        # Salida: 5
print(calculadora(10, 5, 'multiplicacion')) # Salida: 50
print(calculadora(10, 5, 'division'))     # Salida: 2.0
