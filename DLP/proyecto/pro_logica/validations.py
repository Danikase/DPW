# utils.py

import re

# Función para validar correo electrónico
def validar_correo(correo):
    return correo.endswith("@itca.edu.sv")

# Función para validar carné de estudiante
def validar_carnet(carnet):
    return carnet.isdigit() and len(carnet) == 6

# Función para validar contraseña
def validar_contraseña(contraseña):
    if len(contraseña) < 8 or " " in contraseña:
        return False
    if not re.search("[a-zA-Z]", contraseña) or not re.search("[0-9]", contraseña):
        return False
    return True
