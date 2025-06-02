'''
N.-06) Desarrolle un programa amigable para el usuario, en cualquier lenguaje de alto nivel 
o de macros que escoja, para implementar el método de Gauss-Seidel. 
Pruebe el programa con el siguiente sistema (cuya solución es x_1 = 3, ... verificar x_2, x_3):

    3x_1 - 0.1x_2 - 0.2x_3      =   7.85
    0.1x_1 + 7x_2 - 0.3x_3      = -19.3
    0.3x_1 - 0.2x_2 + 10x_3     =  71.4

Utilice como criterio de paro la condición:

    (||x^(k) - x^(k-1)||∞ / ||x^(k)||∞ ) < 10^(-3)

Recuerde que:

Si A = (a_{ij}) es una matriz n x n, entonces ||A||∞ = max(1 <= i <= n) ∑(n hasta j = 1) |a_{ij}| 

Si x = (x_1, x_2, ..., x_n) y y = (y_1, y_2, ..., y_n) son vectores en R^n, la distancia l∞
entre x y y se define mediante  ||x-y|| = max(1 <= i <= n) |x_i - y_i|

'''

import numpy as np
import csv
from decimal import Decimal, getcontext

# Aritmetica de 4 dígitos
getcontext().prec = 4

# Función para calcular la norma infinito de un vector (L∞)
def norma_infinito(vector):
    return max(abs(x) for x in vector)

# Se le pide al usuario el tamaño de la matriz y luego se ingresan los datos de ella
n = int(input("Ingrese el tamaño de la matriz cuadrada (Escriba solo el número, ejemplo: 3): "))
print("Ingrese la matriz A:")
A = np.zeros((n, n), dtype=Decimal)
for i in range(n):
    for j in range(n):
        A[i, j] = Decimal(input(f"A[{i+1},{j+1}]: "))

# Se ingresa el vector b
print("Ingrese el vector b:")
b = np.zeros(n, dtype=Decimal)
for i in range(n):
    b[i] = Decimal(input(f"b[{i+1}]: "))

# Se inicializa el vector de solución x con ceros
x = np.zeros(n, dtype=Decimal)

# Parámetro de tolerancia
tolerancia = Decimal('1e-3')

# Máximo de iteraciones permitidas
max_iteraciones = 1000

csv_file = "resultados_6.csv"
# Crear un archivo CSV para guardar los resultados
with open(csv_file , 'w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Método de Gauss-Seidel
    for iteracion in range(max_iteraciones):
        x_anterior = np.copy(x)
        for i in range(n):
            suma = 0
            for j in range(n):
                if j != i:
                    suma += A[i, j] * x[j]
            x[i] = (b[i] - suma) / A[i, i]

        # Calcula la norma infinito del vector de cambio (numerador de la fracción del criterio de paro)
        norma_cambio = norma_infinito(x - x_anterior)

        # Calcula la norma infinito del vector x (denominador de la fracción del criterio de paro)
        norma_x = norma_infinito(x)

        # Comprueba el criterio de paro
        if norma_cambio / norma_x < tolerancia:
            break

    # Guarda los resultados en el archivo CSV, tanto de [A], vector b y los detalles 
    csv_writer.writerow(["Matriz A"])
    for fila in A:
        csv_writer.writerow([str(valor) for valor in fila])
    csv_writer.writerow([])

    csv_writer.writerow(["Vector b"])
    csv_writer.writerow([str(valor) for valor in b])
    csv_writer.writerow([])

    csv_writer.writerow(["Resultados del método de Gauss-Seidel:"])
    csv_writer.writerow([f"Número de iteraciones: {iteracion + 1}"])
    csv_writer.writerow(["Solución:"])
    for i in range(n):
        csv_writer.writerow([f"x{i + 1}", f"{x[i]}"])

print("El resultado se ha guardado en 'resultados_6.csv'.")
