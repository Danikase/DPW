# menu.py
import os

File_Path = 'DLP/proyecto/books.txt'

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
        print_centered("1. Ver libros")
        print_centered("2. Prestar libros")
        print_centered("3. Devolver libros")
        print_centered("4. Salir")
        print("="*80)
        opcion = input_centered("Seleccione una opción: ")

        if opcion == "1":
            ver_libros()
        elif opcion == "2":
            prestar_libro()
        elif opcion == "3":
            devolver_libro()
        elif opcion == "4":
            break
        else:
            print_centered("Opción inválida. Por favor, seleccione una opción válida.")

# Function to display all available books
def ver_libros():
    clear_screen()
    print_centered("Libros disponibles:")
    try:
        with open(File_Path, 'r') as file:
            books = file.readlines()
            if not books:
                print_centered("No se encontraron libros disponibles.")
            for book in books:
                print_centered(book.strip())
    except FileNotFoundError:
        print_centered("No se encontraron libros disponibles.")
    except Exception as e:
        print_centered(f"Error al leer el archivo: {e}")
    input_centered("Presione Enter para continuar...")

# Function to borrow a book and print a ticket
def prestar_libro():
    global correo, carnet
    clear_screen()
    print_centered("Ingrese el código del libro que desea prestar:")
    codigo = input_centered("Código del libro: ")
    try:
        with open(File_Path, 'r') as file:
            books = file.readlines()
        with open(File_Path, 'w') as file:
            for book in books:
                if not book.startswith(codigo):
                    file.write(book)
                else:
                    print_centered(f"Libro prestado: {book.strip()}")
                    with open('loans.txt', 'a') as loans_file:
                        loans_file.write(f"{correo}:{carnet}:{book.strip()}\n")
                    print_centered("Ticket de préstamo:")
                    print_centered(f"Correo: {correo}")
                    print_centered(f"Carnet: {carnet}")
                    print_centered(f"Libro: {book.strip().split(':')[1]}")
                    print_centered(f"Código: {codigo}")
                    break
            else:
                print_centered("Código de libro no encontrado.")
    except FileNotFoundError:
        print_centered("No se encontraron libros disponibles.")
    except Exception as e:
        print_centered(f"Error al leer el archivo: {e}")
    input_centered("Presione Enter para continuar...")

# Function to return a borrowed book
def devolver_libro():
    global correo, carnet
    clear_screen()
    print_centered("Ingrese el código del libro que desea devolver:")
    codigo = input_centered("Código del libro: ")
    try:
        with open('loans.txt', 'r') as file:
            loans = file.readlines()
        with open('loans.txt', 'w') as file:
            for loan in loans:
                if not loan.split(':')[2].startswith(codigo):
                    file.write(loan)
                else:
                    with open(File_Path, 'a') as books_file:
                        books_file.write(f"{loan.split(':')[2].strip()}\n")
                    print_centered(f"Libro devuelto: {loan.split(':')[2].strip()}")
                    break
            else:
                print_centered("Código de libro no encontrado en los préstamos.")
    except FileNotFoundError:
        print_centered("No se encontraron préstamos.")
    except Exception as e:
        print_centered(f"Error al leer el archivo: {e}")
    input_centered("Presione Enter para continuar...")
