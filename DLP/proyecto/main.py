# main.py

from menu import mostrar_menu_principal, mostrar_submenu
from validations import validar_correo, validar_carnet, validar_contraseña
import os

FILE_NAME = 'users.txt'  # The file where user data is stored

# Function to load users from the file
def cargar_usuarios(file_name):
    if not os.path.exists(file_name):
        return []
    with open(file_name, 'r') as file:
        return [line.strip().split(":") for line in file]

# Function to save users to the file
def guardar_usuarios(file_name, usuarios):
    with open(file_name, 'w') as file:
        for usuario in usuarios:
            file.write(":".join(usuario) + "\n")

# Function to register a new user
def registrar_usuario():
    usuarios = cargar_usuarios(FILE_NAME)
    
    correo = input("Ingrese su correo electrónico: ")
    while not validar_correo(correo):
        print("Correo inválido. Debe ser un correo @itca.edu.sv.")
        correo = input("Ingrese su correo electrónico: ")

    carnet = input("Ingrese su número de carnet estudiantil (6 dígitos): ")
    while not validar_carnet(carnet):
        print("Carnet inválido. Debe contener solo números y ser de 6 dígitos.")
        carnet = input("Ingrese su número de carnet estudiantil (6 dígitos): ")

    contraseña = input("Ingrese su contraseña: ")
    while not validar_contraseña(contraseña):
        print("Contraseña inválida. Debe tener al menos 8 caracteres, sin espacios, y contener al menos una letra y un número.")
        contraseña = input("Ingrese su contraseña: ")

    # Check if the carnet is already in use
    if any(usuario[1] == carnet for usuario in usuarios):
        print("El número de carnet ya está en uso.")
    else:
        usuarios.append([correo, carnet, contraseña])
        guardar_usuarios(FILE_NAME, usuarios)
        print("Usuario registrado exitosamente.")

# Function to login a user
def iniciar_sesion():
    usuarios = cargar_usuarios(FILE_NAME)
    carnet = input("Ingrese su número de carnet estudiantil: ")
    contraseña = input("Ingrese su contraseña: ")

    # Verify the credentials
    for usuario in usuarios:
        if usuario[1] == carnet and usuario[2] == contraseña:
            print("Inicio de sesión exitoso.")
            mostrar_menu_principal()
            return
    print("Carnet o contraseña incorrectos.")

# Function to recover a user's password
def recuperar_contraseña():
    usuarios = cargar_usuarios(FILE_NAME)
    carnet = input("Ingrese su número de carnet estudiantil: ")

    # Find and print the password for the given carnet
    for usuario in usuarios:
        if usuario[1] == carnet:
            print(f"Su contraseña es: {usuario[2]}")
            return
    print("Número de carnet no encontrado.")

# Main function to display the menu and handle user input
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
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
