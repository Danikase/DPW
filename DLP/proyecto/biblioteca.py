file_Name = './DLP/proyecto/users.txt'

def registrar_usuario():
    correo = input("Ingrese su correo electrónico: ")
    carnet = input("Ingrese su número de carnet estudiantil (6 dígitos): ")
    contraseña = input("Ingrese su contraseña: ")
    
    with open(file_Name, "r") as file:
        for line in file:
            user_data = line.strip().split(":")
            if user_data[1] == carnet:
                print("El número de carnet ya está en uso.")
                return

    with open(file_Name, "a") as file:
        file.write(f"{correo}:{carnet}:{contraseña}\n")
    print("¡Usuario registrado correctamente!")

def iniciar_sesion():
    carnet = input("Ingrese su número de carnet estudiantil: ")
    contraseña = input("Ingrese su contraseña: ")

    encontrado = False
    with open(file_Name, "r") as file:
        for line in file:
            user_data = line.strip().split(":")
            if user_data[1] == carnet and user_data[2] == contraseña:
                print("¡Inicio de sesión exitoso!")
                print(f"Datos del usuario: Correo: {user_data[0]}, Carnet: {user_data[1]}")
                encontrado = True
                break

    if not encontrado:
        print("Carnet o contraseña incorrectos.")

def imprimir_usuarios():
    print("Lista de Usuarios Registrados:")
    with open(file_Name, "r") as file:
        for line in file:
            user_data = line.strip().split(":")
            print(f"Correo: {user_data[0]}, Carnet: {user_data[1]}, Contraseña: {user_data[2]}")

# Menú principal
while True:
    print("\n1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Imprimir usuarios")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        imprimir_usuarios()
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
#Codigo chido
