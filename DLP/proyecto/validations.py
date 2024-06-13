import re

# Funcion para validar el email
def validar_correo(correo):
    return correo.endswith("@itca.edu.sv")

# Funcion para validar el Carnet
def validar_carnet(carnet):
    return carnet.isdigit() and len(carnet) == 6

# Funcion para validar la contraseña
def validar_contraseña(contraseña):
    if len(contraseña) < 8 or " " in contraseña:
        return False
    if not re.search("[a-zA-Z]", contraseña) or not re.search("[0-9]", contraseña):
        return False
    return True
#codigo chido