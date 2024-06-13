# utils.py

import re

# Function to validate email
def validar_correo(correo):
    return correo.endswith("@itca.edu.sv")

# Function to validate student ID (carnet)
def validar_carnet(carnet):
    return carnet.isdigit() and len(carnet) == 6

# Function to validate password
def validar_contraseña(contraseña):
    if len(contraseña) < 8 or " " in contraseña:
        return False
    if not re.search("[a-zA-Z]", contraseña) or not re.search("[0-9]", contraseña):
        return False
    return True
