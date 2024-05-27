import re

file_Name = './DLP/proyecto/users.txt'  # Asegúrate de que la ruta del archivo sea correcta

# Función para validar que el correo termine en '@itca.edu.sv'
def validar_correo(correo):
    return correo.endswith("@itca.edu.sv")

# Función para validar que el carnet tenga solo números y sea de 6 dígitos
def validar_carnet(carnet):
    return carnet.isdigit() and len(carnet) == 6

# Función para validar que la contraseña tenga al menos 8 caracteres, sin espacios, y contenga al menos una letra y un número
def validar_contraseña(contraseña):
    if len(contraseña) < 8:
        return False
    if " " in contraseña:
        return False
    if not re.search("[a-zA-Z]", contraseña):
        return False
    if not re.search("[0-9]", contraseña):
        return False
    return True

# Función para registrar un nuevo usuario
def registrar_usuario():
    correo = input("Ingrese su correo electrónico: ")
    while not validar_correo(correo):  # Validar el correo
        print("Correo inválido. Debe ser un correo @itca.edu.sv.")
        correo = input("Ingrese su correo electrónico: ")
    
    carnet = input("Ingrese su número de carnet estudiantil (6 dígitos): ")
    while not validar_carnet(carnet):  # Validar el carnet
        print("Carnet inválido. Debe contener solo números y ser de 6 dígitos.")
        carnet = input("Ingrese su número de carnet estudiantil (6 dígitos): ")
    
    contraseña = input("Ingrese su contraseña: ")
    while not validar_contraseña(contraseña):  # Validar la contraseña
        print("Contraseña inválida. Debe tener al menos 8 caracteres, sin espacios, y contener al menos una letra y un número.")
        contraseña = input("Ingrese su contraseña: ")
    
    # Verificar si el carnet ya está en uso
    try:
        with open(file_Name, "r") as file:
            for line in file:
                user_data = line.strip().split(":")
                if user_data[1] == carnet:
                    print("El número de carnet ya está en uso.")
                    return
    except FileNotFoundError:
        pass

    # Registrar el nuevo usuario
    with open(file_Name, "a") as file:
        file.write(f"{correo}:{carnet}:{contraseña}\n")
    print("¡Usuario registrado correctamente!")

# Función para iniciar sesión
def iniciar_sesion():
    carnet = input("Ingrese su número de carnet estudiantil: ")
    contraseña = input("Ingrese su contraseña: ")

    encontrado = False
    try:
        # Verificar las credenciales del usuario
        with open(file_Name, "r") as file:
            for line in file:
                user_data = line.strip().split(":")
                if user_data[1] == carnet and user_data[2] == contraseña:
                    print("¡Inicio de sesión exitoso!")
                    print(f"Datos del usuario: Correo: {user_data[0]}, Carnet: {user_data[1]}")
                    encontrado = True
                    mostrar_menu_principal()
                    break
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")

    if not encontrado:
        print("Carnet o contraseña incorrectos.")

# Función para imprimir la lista de usuarios registrados
def imprimir_usuarios():
    print("Lista de Usuarios Registrados:")
    try:
        with open(file_Name, "r") as file:
            for line in file:
                user_data = line.strip().split(":")
                print(f"Correo: {user_data[0]}, Carnet: {user_data[1]}, Contraseña: {user_data[2]}")
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")

# Función para recuperar la contraseña del usuario
def recuperar_contraseña():
    correo = input("Ingrese su correo electrónico registrado: ")
    encontrado = False
    try:
        with open(file_Name, "r") as file:
            for line in file:
                user_data = line.strip().split(":")
                if user_data[0] == correo:
                    print(f"Su contraseña es: {user_data[2]}")
                    encontrado = True
                    break
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")

    if not encontrado:
        print("Correo no registrado.")

# Función para eliminar una cuenta (solo admin)
def eliminar_cuenta():
    carnet = input("Ingrese su número de carnet estudiantil: ")
    contraseña = input("Ingrese su contraseña: ")
    admin_pass = input("Ingrese la contraseña de administrador: ")

    if admin_pass != "admin123":  # Verificar la contraseña de admin
        print("Contraseña de administrador incorrecta.")
        return

    usuarios = []
    encontrado = False
    try:
        # Verificar las credenciales del usuario y eliminar la cuenta si son correctas
        with open(file_Name, "r") as file:
            for line in file:
                user_data = line.strip().split(":")
                if user_data[1] == carnet and user_data[2] == contraseña:
                    encontrado = True
                else:
                    usuarios.append(line.strip())
    except FileNotFoundError:
        print("No se encontró el archivo de usuarios.")
        return

    if encontrado:
        with open(file_Name, "w") as file:
            for usuario in usuarios:
                file.write(usuario + "\n")
        print("Cuenta eliminada correctamente.")
    else:
        print("Carnet o contraseña incorrectos.")

# Menú después de iniciar sesión
def mostrar_menu_principal():
    while True:
        print("\n1. Inicio")
        print("2. Todos")
        print("3. Base de datos")
        print("4. Libros Electrónicos")
        print("5. Revistas electrónicas")
        print("6. Cerrar sesión")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_submenu("Inicio")
        elif opcion == "2":
            mostrar_submenu("Todos")
        elif opcion == "3":
            mostrar_submenu("Base de datos")
        elif opcion == "4":
            mostrar_submenu("Libros Electrónicos")
        elif opcion == "5":
            mostrar_submenu("Revistas electrónicas")
        elif opcion == "6":
            print("Sesión cerrada.")
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Submenú para las opciones del menú principal
def mostrar_submenu(titulo):
    while True:
        print(f"\n--- {titulo} ---")
        print("1. Regresar")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            break
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

# Menú inicial
while True:
    print("\n1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Imprimir usuarios")
    print("4. Recuperar contraseña")
    print("5. Eliminar cuenta (Admin)")
    print("6. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        imprimir_usuarios()
    elif opcion == "4":
        recuperar_contraseña()
    elif opcion == "5":
        eliminar_cuenta()
    elif opcion == "6":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
# Codigo chido