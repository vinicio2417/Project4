def mostrar_matriz(matriz, titulo):
    """Función para mostrar una matriz de forma ordenada"""
    print(f"\n{titulo}:")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"{matriz[i][j]:4}", end=" ")
        print()


def bubble_sort_ascendente(arr):
    """Implementación del algoritmo Bubble Sort para ordenar en orden ascendente"""
    n = len(arr)
    # Hacer una copia para no modificar el array original directamente
    arr_copia = arr.copy()

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr_copia[j] > arr_copia[j + 1]:
                # Intercambiar elementos
                arr_copia[j], arr_copia[j + 1] = arr_copia[j + 1], arr_copia[j]

    return arr_copia


def ordenar_fila_matriz(matriz, fila):
    """Función que ordena una fila específica de la matriz"""
    # Validar que la fila existe
    if fila < 0 or fila >= len(matriz):
        print(f"Error: La fila {fila} no existe en la matriz")
        return matriz.copy()

    # Crear una copia de la matriz para no modificar la original
    matriz_copia = [fila_matriz.copy() for fila_matriz in matriz]

    # Ordenar la fila especificada
    matriz_copia[fila] = bubble_sort_ascendente(matriz_copia[fila])

    return matriz_copia


# Crear una matriz 3x3 con valores numéricos
matriz_original = [
    [9, 3, 7],
    [4, 8, 1],
    [6, 2, 5]
]

# Mostrar la matriz original
mostrar_matriz(matriz_original, "Matriz Original")

# Pedir al usuario qué fila quiere ordenar
try:
    fila_a_ordenar = int(input("\n¿Qué fila quieres ordenar? (0-2): "))

    # Ordenar la fila especificada
    matriz_ordenada = ordenar_fila_matriz(matriz_original, fila_a_ordenar)

    # Mostrar la matriz con la fila ordenada
    mostrar_matriz(matriz_ordenada, f"Matriz con la fila {fila_a_ordenar} ordenada")

except ValueError:
    print("Por favor, ingresa un número válido (0, 1 o 2)")