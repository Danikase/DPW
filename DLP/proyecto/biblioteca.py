file_Name = './DLP/proyecto/users.txt'

def registrar_usuario():
    correo = input("Ingrese su correo electrónico: ")
    carnet = int(input("Ingrese su número de carnet estudiantil (6 dígitos): "))
    contraseña = input("Ingrese su contraseña: ")
    

    # Comprobar si el carnet ya está en uso
    with open(file_Name, "r") as file:
        for line in file:
                
            if line.strip().split(":")[1] == carnet:
                print("El número de carnet ya está en uso.")
                print(line.strip().split(":")[0])
                return

    # Agregar el nuevo usuario al archivo
    with open( file_Name, "a") as file:
        file.write(f"{correo}:{carnet}:{contraseña}\n")
    print("¡Usuario registrado correctamente!")

def iniciar_sesion():
    carnet = input("Ingrese su número de carnet estudiantil: ")
    contraseña = input("Ingrese su contraseña: ")

    # Comprobar las credenciales ingresadas
    with open( file_Name, "r") as file:
        for line in file:
            user_data = line.strip().split(":")
            if user_data[0] == carnet and user_data[2] == contraseña:
                print("¡Inicio de sesión exitoso!")
                return
        print("Carnet o contraseña incorrectos.")

# Menú principal
while True:
    print("\n1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        registrar_usuario()
    elif opcion == "2":
        iniciar_sesion()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")
