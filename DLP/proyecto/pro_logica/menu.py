# menu.py
import os

File_Path = 'C:/Users/link3/OneDrive/Documentos/pro_logica/books.txt'

# Función para limpiar la pantalla del terminal
def clear_screen():
    if os.name == 'nt':
        os.system('cls')  # Windows
    else:
        os.system('clear')  # Unix/Linux/Mac

# Función para imprimir texto centrado en el terminal
def print_centered(text):
    terminal_width = 80
    text_width = len(text)
    padding = (terminal_width - text_width) // 2
    print(' ' * padding + text)

# Función para ingresar texto centrado en el terminal
def input_centered(prompt):
    terminal_width = 80
    text_width = len(prompt)
    padding = (terminal_width - text_width) // 2
    return input(' ' * padding + prompt)

# Función para mostrar el menú principal y obtener la entrada del usuario
def mostrar_menu_principal():
    clear_screen()
    print("\n" + "="*80)
    print_centered("1. Registrarse")
    print_centered("2. Iniciar sesión")
    print_centered("3. Recuperar contraseña")
    print_centered("4. Salir")
    print("="*80)
    return input_centered("Seleccione una opción: ")

# Función para mostrar el menú de usuario después de iniciar sesión y manejar la entrada del usuario
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

# Función para mostrar todos los libros disponibles
def ver_libros():
    clear_screen()
    print_centered("Libros disponibles:")

    try:
        with open(File_Path, "r") as archivo:
            books = archivo.readlines()
            if books:
                for book in books:
                    book_info = book.strip().split(":")
                    if book_info[2] == "available":
                        print_centered(f"{book_info[0]}: {book_info[1]}")
            else:
                print_centered("No hay libros disponibles.")
    except FileNotFoundError:
        print_centered("El archivo de libros no se encuentra.")
    except Exception as e:
        print_centered(f"Error al leer el archivo: {e}")
        
    input_centered("Presione Enter para continuar...")

# Función para prestar un libro e imprimir un ticket
def prestar_libro():
    global carnet
    correo = input_centered("Ingrese su correo electrónico: ")
    carnet = input_centered("Ingrese su carnet: ")
    clear_screen()
    print_centered("Ingrese el código del libro que desea prestar:")
    codigo = input_centered("Código del libro: ")
    book_found = False

    try:
        with open(File_Path, 'r') as file:
            books = file.readlines()

        for i, book in enumerate(books):
            book_info = book.strip().split(':')
            if len(book_info) >= 3:
                if book_info[0] == codigo:
                    if book_info[2] == 'available':
                        book_found = True
                        print_centered(f"Libro prestado: {book.strip()}")
                        with open('loans.txt', 'a') as loans_file:
                            loans_file.write(f"{correo}:{carnet}:{book_info[0]}:{book_info[1]}:loaned\n")
                        print_centered("Ticket de préstamo:")
                        print_centered(f"Libro: {book_info[1]}")
                        print_centered(f"Código: {codigo}")
                        print_centered(f"Estudiante: {correo}")
                        book_info[2] = 'loaned'
                        books[i] = ':'.join(book_info) + '\n'
                    else:
                        print_centered("El libro ya está prestado.")
                    break

        if book_found:
            with open(File_Path, 'w') as file:
                file.writelines(books)
        else:
            print_centered("Código de libro no encontrado.")

    except FileNotFoundError:
        print_centered("No se encontraron libros disponibles.")
    except Exception as e:
        print_centered(f"Error al leer el archivo: {e}")

    input_centered("Presione Enter para continuar...")


# Función para devolver un libro prestado
def devolver_libro():
    clear_screen()
    print_centered("Ingrese el código del libro que desea devolver:")
    codigo = input_centered("Código del libro: ")
    found = False

    try:
        with open('loans.txt', 'r') as file:
            loans = file.readlines()

        for i, loan in enumerate(loans):
            loan_info = loan.strip().split(':')
            if loan_info[2] == codigo:
                found = True
                print_centered(f"Libro devuelto: {loan.strip()}")

                # Actualizar estado del libro en books.txt
                with open(File_Path, 'r') as file:
                    books = file.readlines()
                for j, book in enumerate(books):
                    book_info = book.strip().split(':')
                    if book_info[0] == codigo:
                        book_info[2] = 'available'
                        books[j] = ':'.join(book_info) + '\n'
                        break
                with open(File_Path, 'w') as file:
                    file.writelines(books)

                # Eliminar entrada de loans.txt
                del loans[i]
                break

        if found:
            with open('loans.txt', 'w') as file:
                file.writelines(loans)
        else:
            print_centered("Código de libro no encontrado.")

    except FileNotFoundError:
        print_centered("No se encontraron préstamos.")
    except Exception as e:
        print_centered(f"Error al leer el archivo: {e}")

    input_centered("Presione Enter para continuar...")


