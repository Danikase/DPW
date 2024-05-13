animal = input("Introduce el nombre de un animal: ")

match animal:
    case "perro", "gato", "vaca", "elefante", "leon":
        print("El animal es un mamífero.")
    case "aguila", "gorrion", "pato", "pinguino", "buho":
        print("El animal es un ave.")
    case "lagarto", "serpiente", "cocodrilo", "tortuga", "iguana":
        print("El animal es un reptil.")
    case "salmon", "atun", "pez payaso", "anguila", "trucha":
        print("El animal es un pez.")
    case "rana", "salamandra", "sapos", "axolote", "triton":
        print("El animal es un anfibio.")
    case _:
        print("No se reconoce este animal.")
