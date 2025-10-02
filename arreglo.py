# Crear y escribir en un archivo de texto
# El archivo se llamará "my_notes.txt"

# Abrimos el archivo en modo escritura ("w") -> esto crea el archivo o lo sobrescribe
archivo = open("my_notes.txt", "w")

# Escribimos varias líneas de notas personales con write()
archivo.write("Nota 1: Recordar estudiar para el examen de programacion.\n")
archivo.write("Nota 2: revisar las notas en la plataforma eva.\n")
archivo.write("Nota 3: Revisar el correo electrónico de la universidad \n")

# Cerramos el archivo después de escribir
archivo.close()

# Lectura del archivo línea por línea
# Ahora abrimos el archivo en modo lectura ("r")
archivo = open("my_notes.txt", "r")

# Usamos un bucle para leer línea por línea con readline()
linea = archivo.readline()  # Lee la primera línea
while linea != "":  # Mientras no sea fin de archivo
    print(linea.strip())  # strip() elimina saltos de línea extras
    linea = archivo.readline()  # Lee la siguiente línea

# Cerramos el archivo después de leer
archivo.close()