
'''
N.-04) Desarrolle un programa amigable para el usuario, en cualquier lenguaje de alto nivel 
o de macros que elija, para realizar la descomposición LU de Doolittle 
([A] = [L][U]) y obtener la solución del siguiente sistema de ecuaciones:

    x_1  + x_2           + 3x_4  =  8
    2x_1 + x_2   - x_3   + x_4   =  7
    3x1  - x_2   - x_3   + 2x_4  = 14
   -x1   + 2x_2  + 3x_3  - x_4   = -7

'''

import numpy as np
from decimal import Decimal, getcontext
import csv


# Aritmetica de 4 dígitos
getcontext().prec = 4

# Se le pide al usuario el tamaño de la matriz y luego escribe los datos de ella
n = int(input("Ingrese el tamaño de la matriz cuadrada (Escriba solo el número, ejemplo: 4): "))

# Matriz A
#  [1, 1, 0, 3],
# [2, 1, -1, 1],
# [3, -1, -1, 2],
# [-1, 2, 3, -1]

print("Ingrese la matriz A:")
A = np.zeros((n, n), dtype=Decimal)
for i in range(n):
    for j in range(n):
        A[i, j] = Decimal(input(f"A[{i+1},{j+1}]: "))

# vector b
# [8, 7, 14, -7]

print("Ingrese el vector b:")
b = np.zeros(n, dtype=Decimal)
for i in range(n):
    b[i] = Decimal(input(f"b[{i+1}]: "))

# Se crea resultados_4.csv 
csv_file = "resultados_4.csv"
with open(csv_file, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Matriz A"])
    for fila in A:
        csv_writer.writerow([str(valor) for valor in fila])
    csv_writer.writerow([])

    csv_writer.writerow(["Vector b"])
    csv_writer.writerow([str(valor) for valor in b])
    csv_writer.writerow([])

    # Función de descomposición de [A] = [L][U] de Doolittle
    def Doolittle(A, B):
        # Se crean 3 matrices: 
        # n tiene el tamaño de [A], 
        # [L] y [U] tienen el tamaño de la matriz cuadrada con aritmética de 4 dígitos
    
        n = len(A)
        U = np.zeros((n, n), dtype=Decimal)
        L = np.zeros((n, n), dtype=Decimal)


        # se realiza la descomposicion de la matriz A en L y U
        # se itera k para poder realizar la matriz triangular superior
        # The sum() function adds the items of an iterable and returns the sum.
        for k in range(n):

           # Se itera sobre las columnas de [A] y calcula los elementos de la matriz triangular superior U.
            for i in range(k, n):
                U[k][i] = A[k][i] - sum(L[k][p] * U[p][i] for p in range(k))

            # Calculas los elementos de en las columnas de k para la matriz triangular inferior L
            for i in range(k, n):
                # Comprobnamos si el elemento diagonal U[k][k] es igual a cero.
                if U[k][k] == 0:
                    exit()
                # Calcula los elementos de la columna k de la matriz triangular inferior L.
                L[i][k] = (A[i][k] - sum(L[i][p] * U[p][k] for p in range(k))) / U[k][k]

        # sustitución hacia adelante
        # D es un vector temporal que almacena los resultados de la sustitucion hacia adelante
        # por cada iteracion calcula los elementos de D en funcion de la matriz triangular inferior L y vector b
        D = np.zeros(n, dtype=Decimal)
        for i in range(n):
            D[i] = B[i] - sum(L[i][j] * D[j] for j in range(i))

        # sustitución hacia atrás
        # X es un vector temporal que almacena los resultados de la sustitucion hacia adelante
        # por cada iteracion calcula los elementos de X en funcion de la matriz triangular superior U y vector D
        x = np.zeros(n, dtype=Decimal)
        for i in range(n - 1, -1, -1):
            x[i] = (D[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]

        return L, U, x

    # Realiza la descomposición [L][U] de [A]
    L, U, x = Doolittle(A, b)

    # Escribe el paso de la descomposición en el archivo CSV
    csv_writer.writerow(["Matriz L final"])
    for fila in L:
        csv_writer.writerow([str(valor) for valor in fila])
    csv_writer.writerow([])

    csv_writer.writerow(["Matriz U final"])
    for fila in U:
        csv_writer.writerow([str(valor) for valor in fila])
    csv_writer.writerow([])

    csv_writer.writerow(["La solución del sistema de ecuaciones es"])
    for i in range(len(x)):
        csv_writer.writerow([f"x_{i+1} = {x[i]}"])

    # Multiplicación de L y U como comprobación
    LU = np.dot(L, U)
    csv_writer.writerow([])
    csv_writer.writerow(["Multiplicación de L y U"])
    for fila in LU:
        csv_writer.writerow([str(valor) for valor in fila])


print("Resultados guardados en 'resultados_4.csv'")
