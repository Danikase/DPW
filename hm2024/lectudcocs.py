# Define la ruta base de la carpeta
file_path = "C:/Users/henri/OneDrive/Documentos/hm2024"

# Construye la ruta completa al archivo concatenando las cadenas
full_path = file_path + '/archivo.txt'

file = open(full_path, 'r')

content = file.read()
print(content)
file.close()

file = open(file_path + '/archivo2.txt', 'w')
file.write('Hola, mundo!')
file.close()

f = open(file_path + '/archivo3.txt', 'a')
f.write('\n' + 'Hola Mundo')
f.close()