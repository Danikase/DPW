from validations import validar_correo, validar_carnet, validar_contraseña
from menu import mostrar_menu_principal, mostrar_menu_usuario, print_centered, input_centered, clear_screen
import os

# Variable donde se almacena el archivo donde se almacenaran los datos de los usuarios
FILE_NAME = 'users.txt'

def cargar_usuarios(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r') as file:
        return [line.strip().split(":") for line in file]

def guardar_usuarios(file_name, usuarios):
    with open(file_name, 'w') as file:
        for usuario in usuarios:
            file.write(":".join(usuario) + "\n")

def registrar_usuario():
    usuarios = cargar_usuarios(FILE_NAME)
    
    correo = input_centered("Ingrese su correo electrónico: ")
    while not validar_correo(correo):
        print_centered("Correo inválido. Debe ser un correo @itca.edu.sv.")
        correo = input_centered("Ingrese su correo electrónico: ")

    carnet = input_centered("Ingrese su número de carnet estudiantil (6 dígitos): ")
    while not validar_carnet(carnet):
        print_centered("Carnet inválido. Debe contener solo números y ser de 6 dígitos.")
        carnet = input_centered("Ingrese su número de carnet estudiantil (6 dígitos): ")

    contraseña = input_centered("Ingrese su contraseña: ")
    while not validar_contraseña(contraseña):
        print_centered("Contraseña inválida. Debe tener al menos 8 caracteres, sin espacios, y contener al menos una letra y un número.")
        contraseña = input_centered("Ingrese su contraseña: ")

    if any(usuario[1] == carnet for usuario in usuarios):
        print_centered("El número de carnet ya está en uso.")
    else:
        usuarios.append([correo, carnet, contraseña])
        guardar_usuarios(FILE_NAME, usuarios)
        print_centered("Usuario registrado exitosamente.")

def iniciar_sesion():
    usuarios = cargar_usuarios(FILE_NAME)
    carnet = input_centered("Ingrese su número de carnet estudiantil: ")
    contraseña = input_centered("Ingrese su contraseña: ")

    for usuario in usuarios:
        if usuario[1] == carnet and usuario[2] == contraseña:
            print_centered("Inicio de sesión exitoso.")
            mostrar_menu_usuario()
            return
    print_centered("Carnet o contraseña incorrectos.")

def recuperar_contraseña():
    usuarios = cargar_usuarios(FILE_NAME)
    carnet = input_centered("Ingrese su número de carnet estudiantil: ")

    for usuario in usuarios:
        if usuario[1] == carnet:
            print_centered(f"Su contraseña es: {usuario[2]}")
            return
    print_centered("Número de carnet no encontrado.")

def main():
    while True:
        opcion = mostrar_menu_principal()
        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            iniciar_sesion()
        elif opcion == "3":
            recuperar_contraseña()
        elif opcion == "4":
            print_centered("¡Hasta luego!")
            break
        else:
            print_centered("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
