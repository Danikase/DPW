def mostrar_estudiantes(registro):
    for nombre, calificaciones in registro.items():
        print(f"Estudiante: {nombre}, Calificaciones: {calificaciones}")

# Ejemplo de uso:
mostrar_estudiantes(registro_estudiantes)
# Salida:
# Estudiante: Juan, Calificaciones: [80, 90, 100]
# Estudiante: Ana, Calificaciones: [70, 85]
# Estudiante: Luis, Calificaciones: []
