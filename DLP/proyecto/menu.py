# menu.py

import shutil

# Function to print text centered in the terminal
def print_centered(text):
    terminal_size = shutil.get_terminal_size((80, 20))
    terminal_width = terminal_size.columns
    text_width = len(text)
    padding = (terminal_width - text_width) // 2
    print(' ' * padding + text)

# Function to display the main menu and get user input
def mostrar_menu_principal():
    print()
    print_centered("1. Registrarse")
    print_centered("2. Iniciar sesión")
    print_centered("3. Recuperar contraseña")
    print_centered("4. Salir")
    return input("Seleccione una opción: ")

# Function to display a submenu for a given title
def mostrar_submenu(titulo):
    while True:
        print()
        print_centered(f"--- {titulo} ---")
        print_centered("1. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            break
        else:
            print_centered("Opción inválida. Por favor, seleccione una opción válida.")
