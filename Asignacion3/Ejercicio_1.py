"""
N.-01) Desarrolle, depure y pruebe un programa en cualquier lenguaje de alto nivel 
o mediante macros de su preferencia, para realizar la multiplicación de matrices, 
es decir: [X] = [Y] * [Z], donde:

- [Y] es de orden m por n
- [Z] es de orden n por p

Pruebe el programa utilizando las siguientes matrices de ejemplo:

    [A] = {(1,6),      [B] = {(1,6),        [C] = {(2,-2),
           (3, 10),           (0.5, 2)}            (3, 1)}
           (7, 4)}


Ejecute todas las multiplicaciones posibles entre parejas de matrices 
(cuando las dimensiones lo permitan).
"""

# Configura la precisión decimal a 4 dígitos significativos

from decimal import Decimal, getcontext
getcontext().prec = 4

# FUNCIÓN: Multiplicación de matrices con registro de operaciones paso a paso

def multiplicar_matrices(a, b, nombre_a, nombre_b):
    # Verifica que las dimensiones sean compatibles para la multiplicación
    if len(a[0]) != len(b):
        print(f"No se pueden multiplicar {nombre_a} y {nombre_b} debido a dimensiones incorrectas.")
        return None, None
    # Inicializa la matriz resultado con ceros decimales
    n = len(a)
    m = len(b[0])
    c = [[Decimal(0) for _ in range(m)] for _ in range(n)]

    # Lista para almacenar el detalle de cada operación realizada
    cuentas = []

    # Realiza la multiplicación fila por columna
    for i in range(n):
        for j in range(m):
            suma = Decimal(0)
            step = f"Multiplicando fila {i + 1} de {nombre_a} por columna {j + 1} de {nombre_b}:"
            for k in range(len(b)):
                producto = a[i][k] * b[k][j]
                suma += producto
                step += f"\n  - {a[i][k]} * {b[k][j]} = {producto}"
            c[i][j] = suma
            cuentas.append(step)

    return c, cuentas

# FUNCIÓN: Ingreso interactivo de valores para una matriz de tamaño especificado
def ingresar_matriz(filas, columnas, nombre_matriz):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            valor = input(f"Ingrese el valor de la matriz {nombre_matriz} para la posición ({i + 1}, {j + 1}): ")
            try:
                valor = Decimal(valor)
            except ValueError:
                print("El valor ingresado no es válido. Debe ser un número decimal o en notación científica.")
                return ingresar_matriz(filas, columnas, nombre_matriz)
            fila.append(valor)
        matriz.append(fila)
    return matriz

# ENTRADA DE DATOS: Dimensiones y valores para las matrices A, B y C

filas_a = int(input("Ingrese el número de filas de la matriz A: "))
columnas_a = int(input("Ingrese el número de columnas de la matriz A: "))
filas_b = int(input("Ingrese el número de filas de la matriz B: "))
columnas_b = int(input("Ingrese el número de columnas de la matriz B: "))
filas_c = int(input("Ingrese el número de filas de la matriz C: "))
columnas_c = int(input("Ingrese el número de columnas de la matriz C: "))

matriz_a = ingresar_matriz(filas_a, columnas_a, "A")
matriz_b = ingresar_matriz(filas_b, columnas_b, "B")
matriz_c = ingresar_matriz(filas_c, columnas_c, "C")

# INTENTOS DE MULTIPLICACIÓN: Ejecuta las combinaciones posibles entre matrices
# Diccionarios para almacenar resultados y pasos detallados de cada multiplicación

resultados = {}
procesos = {}
multiplicaciones_posibles = []

# Función auxiliar para verificar y realizar una multiplicación

def realizar_multiplicacion(matriz1, matriz2, nombre1, nombre2):
    if len(matriz1[0]) == len(matriz2):
        resultado, proceso = multiplicar_matrices(matriz1, matriz2, nombre1, nombre2)
        if resultado:
            resultados[f"{nombre1} * {nombre2}"] = resultado
            procesos[f"{nombre1} * {nombre2}"] = proceso
            multiplicaciones_posibles.append(f"{nombre1} * {nombre2}")

# Se prueban todas las combinaciones posibles entre A, B y C

realizar_multiplicacion(matriz_a, matriz_b, "A", "B")
realizar_multiplicacion(matriz_a, matriz_c, "A", "C")
realizar_multiplicacion(matriz_b, matriz_a, "B", "A")
realizar_multiplicacion(matriz_b, matriz_c, "B", "C")
realizar_multiplicacion(matriz_c, matriz_a, "C", "A")
realizar_multiplicacion(matriz_c, matriz_b, "C", "B")

# SALIDA DE RESULTADOS: Se guarda en un archivo de texto con formato legible

with open("resultados_1.txt", "w") as file:
    file.write("Matriz A:\n")
    for fila in matriz_a:
        file.write("\t".join([f"{valor:.4f}" for valor in fila]) + "\n")

    file.write("\nMatriz B:\n")
    for fila in matriz_b:
        file.write("\t".join([f"{valor:.4f}" for valor in fila]) + "\n")

    file.write("\nMatriz C:\n")
    for fila in matriz_c:
        file.write("\t".join([f"{valor:.4f}" for valor in fila]) + "\n")

    if multiplicaciones_posibles:
        for key, resultado in resultados.items():
            file.write(f"\nResultado de la multiplicación {key}:\n")
            for fila in resultado:
                file.write("\t".join([f"{valor:.4f}" for valor in fila]) + "\n")
    else:
        file.write("\nNo se pudieron realizar ninguna multiplicación válida.")

    file.write("\nProceso de Multiplicaciones:\n")
    for key, proceso in procesos.items():
        file.write(f"\nProceso de {key}:\n")
        for step in proceso:
            file.write(step + "\n")

# FINALIZACIÓN: Notificación en consola

print("Todo se ha guardado en 'resultados_1.txt'.")

