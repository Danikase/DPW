# menu.py
import os

# Function to clear the terminal screen
def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix/Linux/Mac

# Function to print text centered in the terminal
def print_centered(text):
    terminal_width = 80
    text_width = len(text)
    padding = (terminal_width - text_width) // 2
    print(' ' * padding + text)

# Function to input text centered in the terminal
def input_centered(prompt):
    terminal_width = 80
    text_width = len(prompt)
    padding = (terminal_width - text_width) // 2
    return input(' ' * padding + prompt)

# Function to display the main menu and get user input
def mostrar_menu_principal():
    clear_screen()
    print("\n" + "="*80)
    print_centered("1. Registrarse")
    print_centered("2. Iniciar sesión")
    print_centered("3. Recuperar contraseña")
    print_centered("4. Salir")
    print("="*80)
    return input_centered("Seleccione una opción: ")

# Function to display the user menu after login and handle user input
def mostrar_menu_usuario():
    while True:
        clear_screen()
        print("\n" + "="*80)
        print_centered("1. Ver perfil")
        print_centered("2. Buscar libros")
        print_centered("3. Ver historial")
        print_centered("4. Cerrar sesión")
        print("="*80)
        opcion = input_centered("Seleccione una opción: ")

        if opcion == "1":
            print_centered("Ver perfil seleccionado")
            # Implement the functionality for "Ver perfil"
        elif opcion == "2":
            print_centered("Buscar libros seleccionado")
            # Implement the functionality for "Buscar libros"
        elif opcion == "3":
            print_centered("Ver historial seleccionado")
            # Implement the functionality for "Ver historial"
        elif opcion == "4":
            print_centered("Sesión cerrada.")
            break
        else:
            print_centered("Opción inválida. Por favor, seleccione una opción válida.")
