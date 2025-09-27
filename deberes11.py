# Crear el diccionario pidiendo la información al usuario
informacion_personal = {
    "nombre": input("Ingresa el nombre: "),
    "edad": int(input("Ingresa la edad: ")),
    "ciudad": input("Ingresa la ciudad: "),
    "profesion": input("Ingresa la profesión: ")
}

# Mostrar el diccionario inicial
print("\nDiccionario inicial:")
print(informacion_personal)

# 1. Acceder y modificar el valor de "ciudad"
nueva_ciudad = input("\nIngresa una nueva ciudad para actualizar: ")
informacion_personal["ciudad"] = nueva_ciudad

# 2. Modificar la profesión
nueva_profesion = input("Ingresa una nueva profesión: ")
informacion_personal["profesion"] = nueva_profesion

# 3. Verificar si "telefono" existe, si no, agregarlo
if "telefono" not in informacion_personal:
    telefono = input("Ingresa un número de teléfono ficticio: ")
    informacion_personal["telefono"] = telefono

# 4. Eliminar la clave "edad"
del informacion_personal["edad"]

# 5. Imprimir el diccionario final
print("\nDiccionario final después de todas las operaciones:")
print(informacion_personal)