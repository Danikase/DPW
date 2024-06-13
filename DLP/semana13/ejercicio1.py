def consultar_promedio(registro, nombre):
    if nombre in registro:
        calificaciones = registro[nombre]
        if calificaciones:
            return sum(calificaciones) / len(calificaciones)
        else:
            print(f"El estudiante {nombre} no tiene calificaciones.")
            return None
    else:
        print(f"El estudiante {nombre} no está en el registro.")
        return None

# Ejemplo de uso:
registro_estudiantes = {
    'Juan': [80, 90, 100],
    'Ana': [70, 85],
    'Luis': []
}

print(consultar_promedio(registro_estudiantes, 'Juan'))  # Salida: 90.0
print(consultar_promedio(registro_estudiantes, 'Ana'))   # Salida: 77.5
print(consultar_promedio(registro_estudiantes, 'Luis'))  # Salida: None
print(consultar_promedio(registro_estudiantes, 'Pedro')) # Salida: None
